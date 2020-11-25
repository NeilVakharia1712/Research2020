import numpy as np
from urllib.parse import urlparse
import collections
import operator
import pandas
import matplotlib.pyplot as plt

#Get csv file as a numpy array
my_data = pandas.io.parsers.read_csv("data_edited.csv")
my_data = np.asarray(my_data)

def mostCommonDomain(data):
    all_urls = data[:,3]
    eduDomains = 0
    for i in range(len(all_urls)):
        all_urls[i] = urlparse(str(all_urls[i])).netloc
        if '.edu' in str(all_urls[i]):
            eduDomains += 1


    all_urls = all_urls[all_urls != '']
    count = collections.Counter(all_urls)
    sorted_count = sorted(count.items(), key=operator.itemgetter(1))
    print(sorted_count)
    print(eduDomains)
    total = 0
    for i in range(len(sorted_count)):
        total += sorted_count[i][1]
    print(total)

    for i in sorted_count:
        if "git" in i[0]:
            print(i)
    for i in sorted_count:
        if "stack" in i[0]:
            print(i)




#Function -> kth highest ranks (serp rank k)

def k_highest_ranks(k):
    row_idx = []
    for i in range(len(my_data)):
        if str(my_data[i,10]).isnumeric() and np.int(my_data[i,10]) < k:
            row_idx.append(i)
    row_idx = np.asarray(row_idx)
    return my_data[row_idx]

def max_in_k_queries():
    dat = k_highest_ranks(3)
    mostCommonDomain(dat)


#max_in_k_queries()
#mostCommonDomain(my_data)

'''
x = ["Chegg" ,"Github","CourseHero","StackOverflow", 'Quizlet']
y = [316, 153,  139, 89, 88]


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(x,y)
ax.set_ylabel('# SERPS')
ax.set_title('DOMAIN')
#ax.set_xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
#ax.set_yticks(np.arange(0, 81, 10))
plt.show()

'''

def find_incidence_rate(data, url):
    websites = []
    #websites = set()
    count = 0
    total_num = 0
    stack_over_flow = 0
    for i in range(len(data)):
        if data[i,0] == 'type':
            #if url in websites[:5]:
                #count += 1
            for i in websites[:5]:
                if 'slader' in i:
                    count += 1
                    break

            websites = []
            total_num += 1
        else:
            domain = urlparse(str(data[i,3])).netloc
            websites.append(domain)
    print(total_num, count, stack_over_flow)

def find_incidence_rate_textbook(data, textbook, k):
    websites = []
    count = 0
    total_num = 0
    chegg = 0
    geeksforgeeks = 0
    coursehero = 0
    quizlet = 0
    wikipedia = 0
    stack_overflow = 0
    github = 0
    edu = 0

    for i in range(len(data)):
        if data[i,0] == 'type' and len(websites) > 0:
            if 'www.chegg.com' in websites[:k]:
                chegg += 1
            if 'www.coursehero.com' in websites[:k]:
                coursehero += 1
            if 'www.geeksforgeeks.org' in websites[:k]:
                geeksforgeeks += 1
            if 'quizlet.com' in websites[:k]:
                quizlet += 1
            if 'en.wikipedia.org' in websites[:k]:
                wikipedia += 1
            for i in websites[:k]:
                if 'stackoverflow' in i or 'stackexchange' in i:
                    stack_overflow += 1
                    break
            for i in websites[:k]:
                if 'github' in i:
                    github += 1
                    break
            for i in websites[:k]:
                if '.edu' in i:
                    edu += 1
                    break
            websites = []
            total_num += 1
        elif data[i,12] == textbook:
            domain = urlparse(str(data[i,3])).netloc
            #print(domain)
            websites.append(domain)
    print('textbook', textbook)
    print('K =', k)
    print(total_num)
    print('chegg', chegg, '->',round(chegg/total_num * 100,2))
    print('coursehero', coursehero, '->', round(coursehero / total_num * 100, 2))
    print('quizlet', quizlet, '->', round(quizlet / total_num * 100, 2))
    print('stackoverflow', stack_overflow,'->' , round(stack_overflow/total_num * 100,2))
    print('geeksforgeeks', geeksforgeeks, '->', round(geeksforgeeks / total_num * 100, 2))
    print('wikipedia', wikipedia, '->', round(wikipedia / total_num * 100, 2))
    print('github', github, '->', round(github/total_num * 100,2))
    print('edu', edu, '->', round(edu/total_num * 100, 2))
    print('-----------------------------------------')


#find_incidence_rate_textbook(my_data, 'Modern Operating Systems', 3)
#print(my_data[:,12])
textbooks = ['Modern Operating Systems', 'MIT Algorithms', 'Computer Networking', 'Algorithm Design Manual']
k_values = [10,3,5]

for i in textbooks:
    for k in k_values:
        find_incidence_rate_textbook(my_data, i, k)
