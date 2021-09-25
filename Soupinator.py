import random

fileList = ['savory_soups.txt','creamy_soups.txt','asian_soups.txt']

soupLists = [[],[],[]]

for fileInd in range(len(fileList)):
    file = open(fileList[fileInd],'r')
    for line in file:
        soupLists[fileInd].append(line.strip())

soupMenu = []
totalSoups = len(soupLists[0]) + len(soupLists[1]) + len(soupLists[2])
while len(soupMenu) < (totalSoups):
    print(len(soupMenu))
    for soupInd in range(len(soupLists)):
        if len(soupLists[soupInd]) > 0:
            randomInd = random.randint(0,len(soupLists[soupInd])-1)
            soupMenu.append(soupLists[soupInd][randomInd])
            soupLists[soupInd].pop(randomInd)

for soup in soupMenu:
    print(soup)