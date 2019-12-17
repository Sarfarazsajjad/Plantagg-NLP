import requests
import csv
from bs4 import BeautifulSoup
from simple_chalk import chalk
import time
import re

with open('mgb-data.csv','r',newline='') as inputCSV:
  next(inputCSV)
  readCSV = csv.reader(inputCSV, delimiter=',')
  for data in readCSV:
    common_name = data[1]
    botanical_name = data[2]
    planturl = data[8]
    print(chalk.red.bold(common_name))
    # print(chalk.yellow(botanical_name))
    # print(chalk.green(planturl))
    time.sleep(0.5)
    r = requests.get(planturl)
    soup = BeautifulSoup(r.text,'html.parser')
    plant_data = soup.find('div',{'class','column-right'})


    plant_common_name = soup.find(id="MainContentPlaceHolder_CommonNameRow")
    plant_type = soup.find(id="MainContentPlaceHolder_TypeRow")
    plant_family = soup.find(id="MainContentPlaceHolder_FamilyRow")
    plant_native = soup.find(id="MainContentPlaceHolder_NativeRangeRow")
    plant_zone = soup.find(id="MainContentPlaceHolder_ZoneRow")
    plant_height = soup.find(id="MainContentPlaceHolder_HeightRow")
    plant_spread = soup.find(id="MainContentPlaceHolder_SpreadRow")
    plant_bloom_time = soup.find(id="MainContentPlaceHolder_BloomTimeRow")
    plant_bloom_description = soup.find(id="MainContentPlaceHolder_ColorTextRow")
    plant_bloom_sun = soup.find(id="MainContentPlaceHolder_SunRow")
    plant_bloom_water = soup.find(id="MainContentPlaceHolder_WaterRow")
    plant_bloom_maintainence = soup.find(id="MainContentPlaceHolder_MaintenanceRow")
    # plant_bloom_flower = soup.find(id="")
    # plant_bloom_leaf = soup.find(id="")
    # plant_bloom_other = soup.find(id="")
    # plant_bloom_tolerate = soup.find(id="")
    print(plant_data)
    temp = []
    for element in plant_data:
      text = soup.find('div',{'class','row'})
      if(text):
        temp.append(text.text)
    
    
    line = temp[0].splitlines()
    for element in line:
      if element:
        cleaned = re.sub(' +', ' ',element)
        print(chalk.magenta.bold(cleaned.split(':')))
  
