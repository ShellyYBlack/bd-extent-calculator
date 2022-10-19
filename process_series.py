def process_series(seriesTitle):
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
        if 'Kilobytes' in quantity.next_sibling.text:
            listKB.append(intQuantity)
        if 'Megabytes' in quantity.next_sibling.text:
            listMB.append(intQuantity)
        if 'gigabytes' in quantity.next_sibling.text:
            listGB.append(intQuantity)
        if 'Files' in quantity.next_sibling.text:
            listFiles.append(intQuantity)

    # Get a sum total of the lists
    totalKB = sum(listKB)
    totalMB = sum(listMB)
    totalGB = sum(listGB)
    totalFiles = sum(listFiles)

    # Add up the lists of bytes and files to get grand totals
    totalSizeMB = totalKB/1024+totalMB+totalGB*1024
    print(seriesTitle.text + " has " + str(totalSizeMB) + " MB and " + str(totalFiles) + " files.")
    return [totalSizeMB,totalFiles]