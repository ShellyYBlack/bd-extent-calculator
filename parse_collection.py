from parse_series import parse_series

def parse_collection(soup):

    collectionTotalSizeMB = 0
    collectionTotalFiles = 0
    collectionTitle = soup.select('archdesc > did unittitle')[0].text
    seriesResultList = []
    
    # Get series titles
    seriesTitles = soup.select('dsc > c > did >  unittitle')
    for seriesTitle in seriesTitles:
        seriesTotalMB, seriesTotalFiles, seriesResult = parse_series(seriesTitle,collectionTitle)
        collectionTotalSizeMB = collectionTotalSizeMB + seriesTotalMB
        collectionTotalFiles = collectionTotalFiles + seriesTotalFiles
        seriesResultList.append(seriesResult)
    
    print('"' + collectionTitle + '",' + str(round(collectionTotalSizeMB)) + ',' + str(collectionTotalFiles))
    for seriesResult in seriesResultList:
        print(seriesResult)
        
    return [collectionTotalSizeMB,collectionTotalFiles]

    