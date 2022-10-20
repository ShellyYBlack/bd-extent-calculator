# bd-extent-calculator

This script calculates the total extent in MB and files from the quantity and unittype tags in an EAD XML finding aid. It provides the totals for the entire collection and each series, as well as all the collections.

It has not been tested on EAD3.

1. Install Beautiful Soup: `sudo apt-get install python3-bs4`
2. Downloaded list of finding aid URLs: `wget https://www.lib.ncsu.edu/findingaids/ead.txt`
3. Downloaded all finding aids: `download-EAD.sh`
3. Calculate extents by replacing path to directory and running: `python3 bd-extent-calculator-multi.py /path/to/ead/file/or/dir > output.csv`

You can also run this script on a single EAD XML file.