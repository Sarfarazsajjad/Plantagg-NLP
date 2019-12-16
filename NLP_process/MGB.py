import requests
import csv
from bs4 import BeautifulSoup

not_found = 0
common_found = 0
botanical_found = 0
both_found = 0
status = 0
plant_seach_link = ''

with open('mgb-master.csv','r',newline='') as csvfile:
  next(csvfile)
  readCSV = csv.reader(csvfile, delimiter=',')
  print(readCSV)
  # use with care
  with open('mgb-data.csv','w+',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Wiki link","common name", "botanical name",'status',"common name worked",'botanical name worked',"both worked",'search result url','missouribotanicalgarden url','page data'])
  
  for row in readCSV:
    print(row)
    common_name = row[1]
    botanical_name = row[2]

    common_name_req = {'basic': common_name}
    r = requests.get('http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx', params=common_name_req)
    print('common name search url',r.url)
    soup = BeautifulSoup(r.text,'html.parser')
    span = soup.find(id="dnn_ctr4158_SearchResults_lblNoResults")
    if span:
      print(span)
      if span.text == "We're sorry, but no results were found matching your criteria.  Please revise your search criteria.":
        print('plant not found with common name',common_name)
    else:
      common_found = 1
      results = soup.find('table',{'class':'results'})
      print(results)
      plant_link = soup.find("a",{"id":"MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_TaxonHTMLName_0"})
      print(plant_link['href'])
      plant_seach_link = plant_link['href']

    botanical_name_req = {'basic': botanical_name}
    r = requests.get('http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx', params=botanical_name_req)
    print('botanical name search url',r.url)
    soup = BeautifulSoup(r.text,'html.parser')
    span = soup.find(id="dnn_ctr4158_SearchResults_lblNoResults")
    if span:
      if span.text == "We're sorry, but no results were found matching your criteria.  Please revise your search criteria.":
        #set status 0
        pass
    else:
      # parse the stuff here
      botanical_found = 1
      results = soup.find('table',{'class':'results'})
      print(results)
      plant_link = soup.find("a",{"id":"MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_TaxonHTMLName_0"})
      print(plant_link['href'])
      plant_seach_link = plant_link['href']
        # plant_common_name = soup.find('div',{'id':'MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_CommonNameRow_0'})
        # plant_type = soup.find('div',{'id':'MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_TypeRow_0'})
        # plant_zone = soup.find('div',{'id':'MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_ZoneRow_0'})
        # plant_height = soup.find('div',{'id':'MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_HeightRow_0'})
    
    if botanical_found and common_found:
      both_found = 1
      status = 1
    elif common_found:
      status = 1
    elif botanical_found:
      status = 1 
    else:
      not_found = 1
      status = 0
    
    with open('mgb-data.csv','a') as writeFile:
      writer = csv.writer(writeFile)
      writer.writerow(['',common_name,botanical_name,status,common_found,botanical_found,r.url,both_found,plant_seach_link,''])