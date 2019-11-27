import wikipedia as wikipedia
import csv

def savePages(srNo,pageName,category,wikiLink):
  pageContent = wikipedia.page(pageName).content
  with open('plantData.csv','a',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([srNo,pageName,category,wikiLink,pageContent,""])
    print("saved",pageName)

def loadPlantNames():
  pageCounter = 0
  # Clear the plant data File to prevent data override 
  with open('plantData.csv','w+',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['SR No','PlantName','Category','Wiki link','Page Data',""])

  with open('plantList.csv') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      pageCounter += 1
      pageName = row[1]
      category = row[2]
      wikiLink = row[3]
      if(pageName == 'NILL'):
        pass
      else:
        savePages(pageCounter,pageName,category,wikiLink)


if __name__ == '__main__':
  loadPlantNames()
