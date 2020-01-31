import requests
import csv
from bs4 import BeautifulSoup
import time
from simple_chalk import chalk
import re

siteURL = 'http://www.missouribotanicalgarden.org/'

with open('MBGPlantDatafinal.csv','r',newline='') as csvfile:
  next(csvfile) #skip the header row
  readCSV = csv.reader(csvfile, delimiter=',')

  # clear the existing file data and add header row
  with open('MBGCommonNames.csv','w+',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Plant url','Common name','Common Name - MBG','Botanical name','Botanical Name - MBG','Type','Family','Native range','Zone','Zone low','Zone high','Height','Height low','Height high','Unit','Spread','Spread low','Spread high','Unit','Bloom Time','Bloom Description','Sun','Water','Maintenance','Suggested Use','Flower','Attracts','Fruit','Leaf','Other','Tolerate','Culture','Noteworthy characteristics','Problems','Garden uses','Hummingbirds','Butterflies','Birds','Erosion','Rabbit','Black Walnut','Drought','Clay Soil','Deer','Dry Soil','Shallow-Rocky Soil','Heavy Shade','Wet Soil','Air Pollution',])
  
  for data in readCSV:
    plant_properties = []
    rowText = []
    commonNameOriginal = data[1]
    CommonNameMBG = ''
    botanicalName = data[3]
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
    common_not_found = 0
    common_found = 0

    # Requst the plantFinder for plant based on common name
    common_name_req = {'basic': commonNameOriginal}
    print(chalk.green(commonNameOriginal))
    time.sleep(1)
    r = requests.get('http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx', params=common_name_req)
    # print(chalk.yellow.bold('common name search url'),r.url)
    soup = BeautifulSoup(r.text,'html.parser')
    span = soup.find(id="dnn_ctr4158_SearchResults_lblNoResults")
    if span:
      # print(chalk.red(span.text))
      if span.text == "We're sorry, but no results were found matching your criteria.  Please revise your search criteria.":
        print(chalk.red.bold('plant not found with common name'),commonNameOriginal)
        common_not_found = 1
        with open('MBGCommonNames.csv','a') as writeFile:
          writer = csv.writer(writeFile)
          print(chalk.magenta("Plant was not found on MGB site"))
          writer.writerow(
            ['Not found',
            commonNameOriginal,
            '0',  # Common Name - MGB
            botanicalName,
            '0',  # Botanical Name - MGB
            '0',  # type 
            '0',  # family
            '0',  # native range
            '0',  # zone
            '0',  # zone 
            '0',  # zone low
            '0',  # zone high
            '0',  # height
            '0',  # height low
            '0',  # heigh high
            '0',  # height unit
            '0',  # spread
            '0',  # spread low
            '0',  # spread high
            '0',  # spread unit
            '0',  # bloom time
            '0',  # bloom description 
            '0',  # sun
            '0',  # water
            '0',  # maintainence
            '0',  # suggested use
            '0',  # flower
            '0',  # attracts
            '0',  # fruit
            '0',  # leaf
            '0',  # other
            '0',  # tolerate
            '0',  # culture
            '0',  # note worthy characteristcs
            '0',  # Problems
            '0',  # garden uses
            ''])
    else:
      common_found = 1
      results = soup.find('table',{'class':'results'})
      # print(results)
      plant_link = soup.find("a",{"id":"MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_TaxonHTMLName_0"})
      planturl = plant_link['href']
      print(chalk.green.bold('plant found common name'),commonNameOriginal)
      # now visit the site and get all the data
      r = requests.get(siteURL+planturl)
      soup = BeautifulSoup(r.text,'html.parser')
      botanicalNameSpan = soup.find(id="dnn_srTitle_lblTitle")
      print(chalk.cyan("botanicalNameMGB ") + botanicalNameSpan.text)
      botanicalNameMGB = botanicalNameSpan.text   
      plant_data = soup.find('div',{'class','column-right'})

      for element in plant_data:
        row = soup.find('div',{'class','row'})
        if(row):
          rowText.append(row.text)
    
          line = rowText[0].splitlines()
    
          for element in line:
            if element:
              cleaned = re.sub(' +', ' ',element)
              # print(cleaned)
              splited = cleaned.split(':')
              # print(chalk.magenta.bold(splited))
              if len(splited) > 1:
                # plant_properties.append(splited[1])
                if(splited[0].strip() == 'Common Name'):
                  CommonNameMBG = splited[1]
                if(splited[0].strip() == 'Type'):
                  Type = splited[1]
                if(splited[0].strip() == 'Family'):
                  Family = splited[1]
                if splited[0].strip() == 'Native Range':
                  NativeRange  = splited[1]
                if splited[0].strip() == 'Zone':
                  Zone = splited[1]
                  zoneSplit = Zone.split('to')
                  ZoneLow = zoneSplit[0]
                  ZoneHigh = zoneSplit[1]
                if splited[0].strip() == 'Height':
                  Height = splited[1]
                  heightSplit = Height.split('to')
                  HeightLow = heightSplit[0]
                  removeFeet = heightSplit[1].split()
                  HeightHigh = removeFeet[0]
                  HeightUnit = removeFeet[1]
                if splited[0].strip() == 'Spread':
                  Spread = splited[1]
                  SpreadSplit = Spread.split('to')
                  SpreadLow = SpreadSplit[0]
                  removeFeet = SpreadSplit[1].split()
                  SpreadHigh = removeFeet[0]
                  SpreadUnit = removeFeet[1]
                if splited[0].strip() == 'Bloom Time':
                  BloomTime  = splited[1]
                if splited[0].strip() == 'Bloom Description':
                  BloomDescription  = splited[1]
                if splited[0].strip() == 'Sun':
                  Sun = splited[1]
                if splited[0].strip() == 'Water':
                  Water = splited[1]
                if splited[0].strip() == 'Maintenance':
                  Maintenance = splited[1]
                if splited[0] == 'Suggested Use':
                  SuggestedUse  = splited[1]
                if splited[0] == 'Flower':
                  Flower = splited[1]
                if splited[0] == 'Attracts':
                  Attracts = splited[1]
                if splited[0] == 'Fruit':
                  Fruit = splited[1]
                if splited[0] == 'Leaf':
                  Leaf = splited[1] 
                if splited[0] == 'Other':
                  Other = splited[1]
                if splited[0] == 'Tolerate':
                  Tolerate = splited[1]
          
          culture = soup.find(id="MainContentPlaceHolder_CultureRow")
          noteworthy_characters = soup.find(id="MainContentPlaceHolder_NoteworthyRow")
          problems = soup.find(id="MainContentPlaceHolder_ProblemsRow")
          garden_uses = soup.find(id="MainContentPlaceHolder_GardenUsesRow")
          if culture:
            plant_properties.append(culture.text)
            Culture = culture.text
          else:
            Culture = ''

          if noteworthy_characters:
            plant_properties.append(noteworthy_characters.text)
            NoteworthyCharacteristics = noteworthy_characters.text
          else:
            NoteworthyCharacteristics = ''

          if problems:
            plant_properties.append(problems.text)
            Problems = problems.text
          else:
            Problems = ''

          if garden_uses:      
            plant_properties.append(garden_uses.text)
            GardenUses = garden_uses.text
          else:
            GardenUses = ''
          
      completePlantUrl = siteURL+planturl 
      print(chalk.cyan(siteURL+planturl))
      print(chalk.red(completePlantUrl))
      with open('MBGCommonNames.csv','a') as writeFile:
        writer = csv.writer(writeFile)
        print(common_not_found)
        if (common_not_found == 0):
          writer.writerow(
            [
            completePlantUrl,
            commonNameOriginal,
            CommonNameMBG,
            botanicalName,
            botanicalNameMGB,
            Type,
            Family,
            NativeRange,
            Zone,
            ZoneLow,
            ZoneHigh,
            Height,
            HeightLow,
            HeightHigh,
            HeightUnit,
            Spread,
            SpreadLow,
            SpreadHigh,
            SpreadUnit,
            BloomTime,
            BloomDescription,
            Sun,
            Water,
            Maintenance,
            SuggestedUse,
            Flower,
            Attracts,
            Fruit,
            Leaf,
            Other,
            Tolerate,
            Culture,
            NoteworthyCharacteristics,
            Problems,
            GardenUses,
            ''])
