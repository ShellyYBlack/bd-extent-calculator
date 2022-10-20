from bs4 import BeautifulSoup
from parse_collection import parse_collection
import sys,os,glob

scriptName, path = sys.argv

collectionsTotalSizeMB = 0
collectionsTotalFiles = 0
numberCollections = 0

print("Title,MB,Files")

# Calling each XML file from path to directory
for filename in glob.glob(os.path.join(path,'*.xml')):
    with open(filename, 'r') as f:
        file = f.read()

    soup = BeautifulSoup(file, 'xml')
    grandTotalSizeMB, grandTotalFiles = parse_collection(soup)
    collectionsTotalSizeMB = collectionsTotalSizeMB + grandTotalSizeMB
    collectionsTotalFiles = collectionsTotalFiles + grandTotalFiles
    numberCollections = numberCollections + 1
print('"Total for ' + str(numberCollections) + ' collections",' + str(round(collectionsTotalSizeMB)) + ',' + str(collectionsTotalFiles))