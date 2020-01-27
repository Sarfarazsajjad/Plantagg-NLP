import requests
import csv
from bs4 import BeautifulSoup
import time
from simple_chalk import chalk

plant_seach_link = ''

with open('mbg-master.csv','r',newline='') as csvfile:
  next(csvfile)
  readCSV = csv.reader(csvfile, delimiter=',')
  # print(readCSV)
  # use with care
  # with open('mgb-data.csv','w+',newline='') as csvfile:
    # writer = csv.writer(csvfile)
    # writer.writerow(["Wiki link","common name", "botanical name",'status',"common name worked",'botanical name worked',"both worked",'search result url','missouribotanicalgarden url','page data'])
  
  for row in readCSV:
    common_not_found = 0
    botanical_not_found = 0
    common_found = 0
    botanical_found = 0
    both_found = 0
    status = 0
    # print(row)
    common_name = row[1]
    # common_name = 'Creek Sedge'
    botanical_name = row[2]
    # botanical_name = 'Carex Amphibola'

    common_name_req = {'basic': common_name}
    time.sleep(1)
    r = requests.get('http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx', params=common_name_req)
    # print(chalk.yellow.bold('common name search url'),r.url)
    soup = BeautifulSoup(r.text,'html.parser')
    span = soup.find(id="dnn_ctr4158_SearchResults_lblNoResults")
    if span:
      # print(chalk.red(span.text))
      if span.text == "We're sorry, but no results were found matching your criteria.  Please revise your search criteria.":
        print(chalk.red.bold('plant not found with common name'),common_name)
        common_not_found = 1
    else:
      common_found = 1
      results = soup.find('table',{'class':'results'})
      # print(results)
      plant_link = soup.find("a",{"id":"MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_TaxonHTMLName_0"})
      # print(plant_link['href'])
      plant_seach_link = plant_link['href']
      print(chalk.green.bold('plant found common name'),common_name)

    botanical_name_req = {'basic': botanical_name}
    time.sleep(1)
    r = requests.get('http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx', params=botanical_name_req)
    # print(chalk.yellow.bold('botanical name search url'),r.url)
    soup = BeautifulSoup(r.text,'html.parser')
    span = soup.find(id="dnn_ctr4158_SearchResults_lblNoResults")
    if span:
      print(chalk.blue(span.text))
      if span.text == "We're sorry, but no results were found matching your criteria.  Please revise your search criteria.":
        print(chalk.red.bold('plant not found with botanical name'),botanical_name)
        botainical_not_found = 1
    else:
      # parse the stuff here
      botanical_found = 1
      results = soup.find('table',{'class':'results'})
      # print(results)
      plant_link = soup.find("a",{"id":"MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_TaxonHTMLName_0"})
      # print(plant_link['href'])
      plant_seach_link = plant_link['href']
      print(chalk.green.bold('plant found botanical'),botanical_name)
    
    if botanical_found and common_found:
      both_found = 1
      status = 1
    elif common_found:
      status = 1
    elif botanical_found:
      status = 1 
    else:
      print(chalk.red.bold("plant "),common_name,botanical_name,chalk.red.bold(" not found in data"))
      common_not_found = 1
      botanical_not_found = 1
      both_found = 0
      botanical_found = 0
      common_found = 0
      status = 0
    
    with open('mbg-data.csv','a') as writeFile:
      writer = csv.writer(writeFile)
      print(common_not_found)
      print(botanical_not_found)
      if (common_not_found == 0 or botanical_not_found == 0):
        writer.writerow(['',common_name,botanical_name,status,common_found,botanical_found,both_found,r.url,'http://www.missouribotanicalgarden.org/'+plant_seach_link,''])
      else:
        print(chalk.magenta("Plant was not found on MGB site"))
        writer.writerow(['',common_name,botanical_name,status,common_found,botanical_found,both_found,r.url,'not found',''])
