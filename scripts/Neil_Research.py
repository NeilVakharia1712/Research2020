import WebSearcher as ws
import os
import csv
import time


def search(query, file, num):
    parent_dir = 'RawHTML/' + file
    dir = str(num)
    path = os.path.join(parent_dir, dir)
    os.mkdir(path)
    se = ws.SearchEngine()
    se.search(query)
    soup = ws.make_soup(se.html)
    results = ws.parse_serp(soup)
    se.save_serp(save_dir=path)
    results = [dict(item, question_number=num) for item in results]
    return results


def getQueries():
    path = 'ResearchQueries'
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(onlyfiles)
    return
    for k in range(12, len(onlyfiles)):
        file = onlyfiles[k]
        file_path = path + '/' + file
        file = file.split('.')
        file = file[0]
        f = open(file_path, "r")
        text = f.read()
        text = text.split("\n\n")
        for i in range(len(text)):
            text[i] = text[i].replace('\n', ' ')
            time.sleep(30)
            data = search(text[i], file, i + 1)
            try:
                copy_to_csv(data)
            except Exception as e:
                print(e)
                print(onlyfiles[k], print(i), print(text))


def copy_to_csv(dict_list):
    keys = dict_list[0].keys()
    with open('data.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(dict_list)


getQueries()
