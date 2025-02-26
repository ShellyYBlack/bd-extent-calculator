# bd-extent-calculator

This script calculates the total extent in MB, files, and websites from the quantity and unittype tags in EAD3 XML finding aids. It provides the totals for the entire collection and each series, as well as all the collections. 

1. Clone the repository:
    `git clone https://github.com/ShellyYBlack/bd-extent-calculator.git`
    * Alternatively, you can also click the green <> Code button and download a ZIP of the files.
1. Change to the born-digital-reporting directory: `cd bdap-reporting`
1. Build the image: `docker build -t bd-reports .`
1. Download finding aid/s:
    * To download all finding aids, run:
    
    `docker run -v $PWD/EAD-XML:/EAD-XML/ -it bd-reports bash -c "wget https://www.lib.ncsu.edu/findingaids/ead.txt ; cd /EAD-XML ; bash /src/download-EAD.sh"` 
    * To download a single finding aid, edit the collection IDs in this command, then run it:

    `docker run -v $PWD/EAD-XML:/EAD-XML/ -it bd-reports bash -c "cd /EAD-XML ; wget -O mc00467.xml https://www.lib.ncsu.edu/findingaids/mc00467/ead"`

1. Calculate extents by replacing path to directory and running:
    
    `docker run -v $PWD/EAD-XML:/EAD-XML/ -it bd-reports bash -c "python3 bd-extent-calculator.py /EAD-XML > /EAD-XML/output.csv"`

## Tips
- If you want to run the script on a single EAD XML file instead of a directory, in step 4, replace /EAD-XML with your file path.
- If you only need to view the results in the terminal, in step 4, you can remove the `>` operator and what follows it.
- This script works on EAD3 records that use \<c\> elements, rather than \<cxx\>. It was also written for records that do not have the id or level attributes in \<c\> elements.
