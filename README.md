# bd-extent-calculator

This script calculates the total extent in MB and files from the quantity and unittype tags in an EAD finding aid. It has not been tested on EAD3.

1. Install Beautiful Soup: `sudo apt-get install python3-bs4`
2. Download EAD finding aid: `wget -O mc00467.xml https://www.lib.ncsu.edu/findingaids/mc00467/ead`
3. Edit your EAD file path and the name of your series in `python3 parsing_ead.py`
4. Run the script.

## TODO
Calculate extents for each series and the whole collection.
