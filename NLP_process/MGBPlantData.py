
import requests
import csv
from bs4 import BeautifulSoup
import time
from simple_chalk import chalk
import re

# navigate to the blank search 
# once for 1336 times
# pick urls of plants and save in MBGPlantSiteUrls.csv
# clear the existing file data and add header row
with open('MBGPlantSiteUrls.csv','w+',newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['MGB Plant Url'])
  
mainPlantsPage = 'https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx'

# its n-1 at the end
for plant in range(1):
  CommonNameMBG = ''
  botanicalNameMGB = ''
  Type = ''
  Family = ''
  NativeRange = ''
  Zone = ''
  ZoneLow = ''
  ZoneHigh = ''
  Height = ''
  HeightLow = ''
  HeightHigh = ''
  HeightUnit = ''
  Spread = ''
  SpreadLow = ''
  SpreadHigh = ''
  SpreadUnit = ''
  BloomTime = ''
  BloomDescription = ''
  Sun = ''
  Water = ''
  Maintenance = ''
  SuggestedUse = ''
  Flower = ''
  Attracts = ''
  Fruit = ''
  Leaf = ''
  Other = ''
  Tolerate = ''
  Culture = ''
  NoteworthyCharacteristics = ''
  Problems = ''
  GardenUses = ''
  plantDetailURLs = []

  # get the first mian page 
  r = requests.get(mainPlantsPage)
  soup = BeautifulSoup(r.text,'html.parser')

  # Each page has 6 plants per page last one 1336 has 4 pants
  # Change range + 1 for each new row of plants added per page like range(4) if plants per page are 8 
  for plantLink in range(3):
    plant_link = soup.find("a",{"id":"MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_" + str(plantLink) + "_TaxonHTMLName_" + str(plantLink)})
    planturl = plant_link['href']
    # print(planturl)
    # This is the complete link to the individual plant
    completePlantUrl = 'https://www.missouribotanicalgarden.org' + planturl
    # print(plantDetailURL)
    plantDetailURLs.append(completePlantUrl)

    plant_link = soup.find("a",{"id":"MainContentPlaceHolder_SearchResultsList_SearchResultControlRight_" + str(plantLink) + "_TaxonHTMLName_" + str(plantLink)})
    planturl = plant_link['href']
    # print(planturlLeft)
    # This is the complete link to the individual plant
    completePlantUrl = 'https://www.missouribotanicalgarden.org' + planturl
    plantDetailURLs.append(completePlantUrl)

  for x in plantDetailURLs:
    with open('MBGPlantSiteUrls.csv','a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow([x])

