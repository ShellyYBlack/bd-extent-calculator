from process_series import process_series

def process_collection(soup):

    grandTotalSizeMB = 0
    grandTotalFiles = 0

    collectionTitle = soup.select('archdesc > did unittitle')[0].text
    print('')
    print(collectionTitle)
    # Get series titles
    seriesTitles = soup.select('dsc > c > did >  unittitle')
    for seriesTitle in seriesTitles:
        totalSizeMB, totalFiles = process_series(seriesTitle)
        grandTotalSizeMB = grandTotalSizeMB + totalSizeMB
        grandTotalFiles = grandTotalFiles + totalFiles
    print("This collection has " + str(grandTotalSizeMB) + " MB and " + str(grandTotalFiles) + " files.")
    return [grandTotalSizeMB,grandTotalFiles]