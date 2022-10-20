import re

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

    # For each quantity tag, if its next sibling (unittype tag) has '...bytes' or 'Files' add to list
    listKB = []
    listMB = []
    listGB = []
    listFiles =[]
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

    # Get a sum total of the lists
    totalKB = sum(listKB)
    totalMB = sum(listMB)
    totalGB = sum(listGB)
    seriesTotalFiles = sum(listFiles)

    # Add up the lists of bytes and files to get grand totals
    seriesTotalMB = totalKB/1024+totalMB+totalGB*1024
    seriesResult = '"' + collectionTitle + '/' + seriesTitle.text + '"' + ',' + str(round(seriesTotalMB)) + ',' + str(seriesTotalFiles)
    return [seriesTotalMB,seriesTotalFiles,seriesResult]
