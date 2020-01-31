import csv
from bs4 import BeautifulSoup
from simple_chalk import chalk

headerRow = []

# use when update common name based data
# with open('MBGCommonNamesV2.csv','w+',newline='') as csvfile:
    # writer = csv.writer(csvfile)
    # writer.writerow(['Plant url','Common name','Common Name - MBG','Botanical name','Botanical Name - MBG','Type','Family','Native range','Zone','Zone low','Zone high','Height','Height low','Height high','Unit','Spread','Spread low','Spread high','Unit','Bloom Time','Bloom Description','Sun','Water','Maintenance','Suggested Use','Flower','Attracts','Fruit','Leaf','Other','Tolerate','Culture','Noteworthy characteristics','Problems','Garden uses','Hummingbirds','Butterflies','Birds','Erosion','Rabbit','Black Walnut','Drought','Clay Soil','Deer','Dry Soil','Shallow-Rocky Soil','Heavy Shade','Wet Soil','Air Pollution',])
  

# use when updating botanical name based data
# with open('MBGBotanicalNamesV2.csv','w+',newline='') as csvfile:
    # writer = csv.writer(csvfile)
    # writer.writerow(['Plant url','Common name','Common Name - MBG','Botanical name','Botanical Name - MBG','Type','Family','Native range','Zone','Zone low','Zone high','Height','Height low','Height high','Unit','Spread','Spread low','Spread high','Unit','Bloom Time','Bloom Description','Sun','Water','Maintenance','Suggested Use','Flower','Attracts','Fruit','Leaf','Other','Tolerate','Culture','Noteworthy characteristics','Problems','Garden uses','Hummingbirds','Butterflies','Birds','Erosion','Rabbit','Black Walnut','Drought','Clay Soil','Deer','Dry Soil','Shallow-Rocky Soil','Heavy Shade','Wet Soil','Air Pollution',])
  

# with open('MBGBotanicalNames.csv','r',newline='') as csvfile:
# with open('MBGCommonNames.csv','r',newline='') as csvfile:
with open('MBGPlantDatafinal.csv','r',newline='') as csvfile:
  
  reader = csv.reader(csvfile, delimiter=',')
  headerRow = next(csvfile)
  # headerRow += ','
  # print(headerRow)
  attractsUnique = []
  tolerateUnique = []

  
  for data in reader:
    attracts = data[26]
    attracts_elements = attracts.split(',')
    Hummingbirds = 0
    Butterflies = 0
    Hummingbirds = 0
    Butterflies = 0
    Birds = 0
    Erosion = 0
    Rabbit = 0
    BlackWalnut = 0
    Drought = 0
    ClaySoil = 0
    Deer = 0
    DrySoil = 0
    ShallowRockySoil = 0
    HeavyShade = 0
    WetSoil = 0
    AirPollution = 0
    for ele in attracts_elements:
      cleaned = ele.strip()
      # if cleaned in attractsUnique:
        # pass
      # else:
        # if cleaned != '':
          # attractsUnique.append(cleaned)
      
      if cleaned == 'Hummingbirds':
        Hummingbirds = 1
      elif cleaned == 'Butterflies':
        Butterflies = 1 
      elif cleaned == 'Birds':
        Birds = 1
      else:
        print(chalk.red('nothing found'),data[1])
    
    tolerate = data[30]
    tolerate_elements = tolerate.split(',')
    for ele in tolerate_elements:
      cleaned = ele.strip()
      if cleaned in tolerateUnique:
        pass
      else:
        if cleaned != '':
          tolerateUnique.append(cleaned)

      if cleaned == 'Erosion':
        Erosion = 1
      elif cleaned == 'Rabbit':
        Rabbit = 1 
      elif cleaned == 'Black Walnut':
        BlackWalnut = 1
      elif cleaned == 'Drought':
        Drought = 1
      elif cleaned == 'Clay Soil':
        ClaySoil = 1
      elif cleaned == 'Deer':
        Deer = 1
      elif cleaned == 'Dry Soil':
        DrySoil = 1
      elif cleaned == 'Shallow-Rocky Soil':
        ShallowRockySoil = 1
      elif cleaned == 'Heavy Shade':
        HeavyShade = 1
      elif cleaned == 'Wet Soil':
        WetSoil = 1
      elif cleaned == 'Air Pollution':
        AirPollution = 1
      else:
        print(chalk.red('nothing found'),data[1])

    # with open('MBGBotanicalNamesV2.csv','a',newline='') as csvfile:
    # with open('MBGCommonNamesV2.csv','a',newline='') as csvfile:
    with open('MBGPlantDataV2.csv','a',newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow([
        data[0],
        data[1],
        data[2],
        data[3],
        data[4],
        data[5],
        data[6],
        data[7],
        data[8],
        data[9],
        data[10],
        data[11],
        data[12],
        data[13],
        data[14],
        data[15],
        data[16],
        data[17],
        data[18],
        data[19],
        data[20],
        data[21],
        data[22],
        data[23],
        data[24],
        data[25],
        attracts,
        data[27],
        data[28],
        data[29],
        data[30],
        data[31],
        data[32],
        data[33],
        data[34],
        Hummingbirds,
        Butterflies,
        Birds,
        Erosion,
        Rabbit,
        BlackWalnut,
        Drought,
        ClaySoil,
        Deer,
        DrySoil,
        ShallowRockySoil,
        HeavyShade,
        WetSoil,
        AirPollution
      ])


# use only to added new columns in sheet dynamically

# print(chalk.red.bold(attractsUnique),len(attractsUnique))
# print(chalk.green.bold(tolerateUnique),len(tolerateUnique))
# 
# for value in attractsUnique:
#   headerRow += value + ','

# for value in tolerateUnique:
#   headerRow += value + ','


# print(headerRow)
# with open('MGBPlantDataV2.csv','w',newline='') as csvfile:
#   writer = csv.writer(csvfile)
#   writer.writerow([headerRow])