from bs4 import BeautifulSoup
from parse_collection import parse_collection
import sys

scriptName, path = sys.argv

with open(path, 'r') as f:
    file = f.read()

soup = BeautifulSoup(file, 'xml')
parse_collection(soup)

