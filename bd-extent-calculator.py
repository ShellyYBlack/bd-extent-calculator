from bs4 import BeautifulSoup
import sys,os,glob,re

# This parses the series
def parse_series(seriesTitle, collectionTitle):
    did = seriesTitle.parent

    # Create a list of c tags or file records
    listFileRecords =[]
    for sibling in did.next_siblings:
        listFileRecords.append(sibling)

    # Create a list of all the quantity tags
    listQuantity =[]
    for c in listFileRecords:
        for quantity in c.findAll('quantity'):
            listQuantity.append(quantity)

    # For each quantity tag, if its next sibling (unittype tag) has bytes/files/websites, add to list
    listKB = []
    listMB = []
    listGB = []
    listFiles =[]
    listWebsites = []
    for quantity in listQuantity:
        intQuantity = eval(quantity.text)
        if re.search('[kK]ilobytes?', quantity.next_sibling.text):
            listKB.append(intQuantity)
        if re.search('[mM]egabytes?', quantity.next_sibling.text):
            listMB.append(intQuantity)
        if re.search('[gG]igabytes?', quantity.next_sibling.text):
            listGB.append(intQuantity)
        if re.search('[fF]iles?', quantity.next_sibling.text):
            listFiles.append(intQuantity)
        if re.search('[wW]ebsites?', quantity.next_sibling.text):
            listWebsites.append(intQuantity)

    # Get a sum total of the lists
    totalKB = sum(listKB)
    totalMB = sum(listMB)
    totalGB = sum(listGB)
    seriesTotalFiles = sum(listFiles)
    seriesTotalWeb = sum(listWebsites)

    # Add up the lists of bytes, files, and websites to get grand totals
    seriesTotalMB = totalKB/1024+totalMB+totalGB*1024
    seriesResult = '"' + collectionTitle + '/' + seriesTitle.text + '"' + ',' + str(round(seriesTotalMB)) + ',' + str(seriesTotalFiles) + ',' + str(seriesTotalWeb)
    return [seriesTotalMB,seriesTotalFiles,seriesTotalWeb,seriesResult]

# This parses the collection
def parse_collection(soup):

    collectionTotalSizeMB = 0
    collectionTotalFiles = 0
    collectionTotalWeb = 0
    collectionTitle = soup.select('archdesc > did unittitle')[0].text
    seriesResultList = []
    
    # Get series titles
    seriesTitles = soup.select('dsc > c > did >  unittitle')
    for seriesTitle in seriesTitles:
        seriesTotalMB, seriesTotalFiles, seriesTotalWeb, seriesResult = parse_series(seriesTitle,collectionTitle)
        collectionTotalSizeMB = collectionTotalSizeMB + seriesTotalMB
        collectionTotalFiles = collectionTotalFiles + seriesTotalFiles
        collectionTotalWeb = collectionTotalWeb + seriesTotalWeb
        seriesResultList.append(seriesResult)
    
    print('"' + collectionTitle + '",' + str(round(collectionTotalSizeMB)) + ',' + str(collectionTotalFiles) + ',' + str(collectionTotalWeb))
    for seriesResult in seriesResultList:
        print(seriesResult)
        
    return [collectionTotalSizeMB,collectionTotalFiles, collectionTotalWeb]

# Main script
scriptName, path = sys.argv
parseOneEAD = path.endswith('.xml')

print("Title,MB,Files,Websites")

if parseOneEAD:
    with open(path, 'r') as f:
        file = f.read()

    soup = BeautifulSoup(file, 'xml')
    parse_collection(soup)
else:
    collectionsTotalSizeMB = 0
    collectionsTotalFiles = 0
    collectionsTotalWeb = 0
    numberCollections = 0
    fileNameList = glob.glob(os.path.join(path,'*.xml'))

    if len(fileNameList) == 0:
        print("There were no XML files in this directory.")
        sys.exit()

    # Calling each XML file from path to directory
    for filename in fileNameList:
        with open(filename, 'r') as f:
            file = f.read()

        soup = BeautifulSoup(file, 'xml')
        grandTotalSizeMB, grandTotalFiles, grandTotalWeb = parse_collection(soup)
        collectionsTotalSizeMB = collectionsTotalSizeMB + grandTotalSizeMB
        collectionsTotalFiles = collectionsTotalFiles + grandTotalFiles
        collectionsTotalWeb = collectionsTotalWeb + grandTotalWeb
        numberCollections = numberCollections + 1
    print('"Total for ' + str(numberCollections) + ' collections",' + str(round(collectionsTotalSizeMB)) + ',' + str(collectionsTotalFiles) + ',' + str(collectionsTotalWeb))