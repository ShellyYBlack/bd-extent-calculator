from bs4 import BeautifulSoup
from process_collection import process_collection
import sys,os,glob

scriptName, path = sys.argv

grandGrandTotalSizeMB = 0
grandGrandTotalFiles = 0
numberCollections = 0

print("Searching " + path)

# Calling each XML file from path to directory
for filename in glob.glob(os.path.join(path,'*.xml')):
    with open(filename, 'r') as f:
        file = f.read()

    soup = BeautifulSoup(file, 'xml')
    grandTotalSizeMB, grandTotalFiles = process_collection(soup)
    grandGrandTotalSizeMB = grandGrandTotalSizeMB + grandTotalSizeMB
    grandGrandTotalFiles = grandGrandTotalFiles + grandTotalFiles
    numberCollections = numberCollections + 1
print("\n" + "There are " + str(numberCollections) + " collections, totaling " + str(round(grandGrandTotalSizeMB)) + " MB and " + str(grandGrandTotalFiles) + " files.")