# bd-extent-calculator

This script calculates the total extent in MB and files from the quantity and unittype tags in an EAD finding aid. It provides the totals for the entire collection and each series, as well as all the collections.

It has not been tested on EAD3.

1. Install Beautiful Soup: `sudo apt-get install python3-bs4`
2. Download EAD finding aid: `wget -O [collection ID].xml [URL]`
3. Run `python3 parsing_ead.py /path/to/ead/file/or/dir`