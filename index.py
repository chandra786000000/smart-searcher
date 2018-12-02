import os
import glob
import re

def build_list(filenames):
    file_terms = {}
    for file in filenames:
        pattern = re.compile('[\W_]+')
        file_terms[file] = open(file, 'r').read().lower();
        file_terms[file] = pattern.sub(' ', file_terms[file])
        re.sub(r'[\W_]+', '', file_terms[file])
        file_terms[file] = file_terms[file].split()
    return file_terms


def indexer_for_file(wordlist):
    fileIndex = {}
    for index,word in enumerate(wordlist):
        if word in fileIndex.keys():
            fileIndex[word].append(index)
        else:
            fileIndex[word] = [index]
    return fileIndex

def make_index(wordlist1):
    result = {}
    for filename in wordlist1.keys():
        result[filename] = indexer_for_file(wordlist1[filename])
    return result

#to construct the inverted index from index
def inverted(total):
    inverted_result = {}
    for filename1 in total.keys():
        for word1 in total[filename1].keys():
            if word1 in total[filename1].keys():
                     if filename1 in total[filename1].keys():
                         inverted_result[word1][filename1].extend(total[filename1][word1][:])
                     else:
                         inverted_result[word1][filename1] = total[filename1][word1]
            else:
                     inverted_result[word1] = {filename1: total[filename1][word1]}
    return inverted_result


path = '/home/chandra/PycharmProjects/change_cips/160101023'
filenames = glob.glob('/home/chandra/PycharmProjects/change_cips/160101023/*.c')
file_terms = build_list(filenames)
total1 = make_index() #give the input for this function


