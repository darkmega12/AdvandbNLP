import csv
import FileManipulation as fileM
import TweetAnalysis as analysis
#import graph as graphing
#from collections import Counter

#filename = 'C:\\Users\\Kiel\\Dropbox\\3RD YEAR\\2ND TERM\\ADVANDB\\filtered-may1-onwards.csv'
filename = 'filtered-may1-onwards.csv'
Data = []
nameList = []
dictList = []

with open ('dictlist.txt', 'r') as f:
    dictList = [line.strip() for line in f]

print("Hello")
Data = fileM.getDataFromCSV(filename)
#for chunk in Data:
#    tempNameStorage = analysis.getInitialNames(chunk)
#    for name in tempNameStorage:
#        nameList.append(name)

nameList = analysis.getInitialNames(Data[5])

nameList = analysis.filterEnglishWords(nameList, dictList)

#graphing.getGraph(Data)
#print (Counter(nameList))
#print (dictList)
#print(duplicateList)
print(nameList)
