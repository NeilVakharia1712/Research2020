import WebSearcher as ws
import os
import csv


# Initialize search engine crawler
# se = ws.SearchEngine()
# Conduct search and retrieve data
# se.search('Prove that the intersection of (0,1/n) for all from n = 1 to inf is 0. Notice that this demonstrates that the intervals in the Nested Interval Property must be closed for the conclusion of the theorem to hold')
# soup = ws.make_soup(se.html)
# Parse the SERP
# results = ws.parse_serp(soup)
# for i in range(5):
# print(results[i])


def search(query):
    se = ws.SearchEngine()
    se.search(query)
    soup = ws.make_soup(se.html)
    results = ws.parse_serp(soup)
    return results


def getQueries():
    isFirstQuery = True
    path = 'ResearchQueries'
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

    for file in onlyfiles:
        file_path = path + '/' + file
        f = open(file_path, "r")
        text = f.read()
        text = text.split("\n\n")
        for i in range(len(text)):
            text[i] = text[i].replace('\n', ' ')
            data = search(text[i])
            copy_to_csv(isFirstQuery, data)
            isFirstQuery = False
        break


def copy_to_csv(write_header, dict_list):

    keys = dict_list[0].keys()
    with open('ResearchQueries/data.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(dict_list)

getQueries()
