import sys
import re
#from porterstemmer import PorterStemmer
import copy

#porter = PorterStemmer()

class queryindex:
    def __init__(self):
        self.index={}

    def readIndex(self):
        f = open(self.index_file , 'r')
        for line in f:
            line = line.rstrip()
            term,pos = line.split('|') #term = term , position = 'docID1:posi1,posi2 ; docID2:posi1,posi2'
            pos = pos.split(';')
            pos = [x.split(':') for x in pos]
            
    def getparamiters(self):
        paramiters = sys.argv
        self.stop_words_files = paramiters[0]
        self.index_file = paramiters[1]

    def Query(self):
        self.getparamiters()
        self.readIndex()

def main():
    q = queryindex()
    q.Query()


