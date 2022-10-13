from bs4 import BeautifulSoup

# Edit the path to your EAD file
with open('/syblack/Downloads/bush.xml', 'r') as f:
    file = f.read()

soup = BeautifulSoup(file, 'xml')

# Replace string with your series title
seriesTitle = soup.find('unittitle', string="Digital Media")
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
    if 'Kilobytes' in quantity.next_sibling.text:
        listKB.append(quantity.text)
    if 'Megabytes' in quantity.next_sibling.text:
        listMB.append(quantity.text)
    if 'gigabytes' in quantity.next_sibling.text:
        listGB.append(quantity.text)
    if 'Files' in quantity.next_sibling.text:
        listFiles.append(quantity.text)

# Turn strings into integers in the lists
listKBint = [eval(i) for i in listKB]
listMBint = [eval(i) for i in listMB]
listGBint = [eval(i) for i in listGB]
listFiles = [eval(i) for i in listFiles]

# Get a sum total of the integers in the lists
totalKB = sum(listKBint)
totalMB = sum(listMBint)
totalGB = sum(listGBint)
totalFiles = sum(listFiles)
print(totalGB)

# Add up the lists of bytes and files to get grand totals
extent = totalKB/1000+totalMB+totalGB*1000
print("This series has " + str(extent) + " MB and " + str(totalFiles) + " files.")
