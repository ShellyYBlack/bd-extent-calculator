# bd-extent-calculator

This script calculates the total extent in MB and files from the quantity and unittype tags in EAD XML finding aids. It provides the totals for the entire collection and each series, as well as all the collections.

Note: This script works on EAD records. It also works on EAD3 records that use \<c\> elements, rather than \<cxx\>.

1. Install Beautiful Soup: `sudo apt-get install python3-bs4`
2. Download a list of your finding aid URLs: `wget https://www.lib.ncsu.edu/findingaids/ead.txt`
3. Run this script to download all your finding aids: `download-EAD.sh`
3. Calculate extents by replacing path to directory and running: `python3 bd-extent-calculator.py /path/to/dir > output.csv`

You can also run this script on a single EAD XML file.