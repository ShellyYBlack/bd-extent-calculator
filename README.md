# bd-extent-calculator

This script calculates the total extent in MB, files, and websites from the quantity and unittype tags in EAD XML finding aids. It provides the totals for the entire collection and each series, as well as all the collections. 

1. Change to your directory containing the Dockerfile.
2. Build the image: `docker build -t bd-extent-calc .`
3. Download finding aids: `docker run -v $PWD/EAD-XML:/EAD-XML/ -it bd-extent-calc bash -c "wget https://www.lib.ncsu.edu/findingaids/ead.txt ; cd /EAD-XML ; bash /src/download-EAD.sh"` 
4. Calculate extents by replacing path to directory and running: `python3 bd-extent-calculator.py /EAD-XML > /EAD-XML/output.csv`

## Tips
- If you want to run the script on a single EAD XML file instead of a directory, in step 4, replace /EAD-XML with your file path.
- If you only need to view the results in the terminal, in step 4, you can remove the `>` operator and what follows it.
- This script works on EAD records. It also works on EAD3 records that use \<c\> elements, rather than \<cxx\>.