from bs4 import BeautifulSoup
from process_collection import process_collection
import sys

scriptName, path = sys.argv

# Edit the path to your EAD file
with open(path, 'r') as f:
    file = f.read()

soup = BeautifulSoup(file, 'xml')
process_collection(soup)