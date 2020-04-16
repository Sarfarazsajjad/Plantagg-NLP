# %%
import wikipedia as wikipedia
import csv
# %%
# prepare csv header
with open('wikipedia_pages_by_plant_botanical_names.csv','a') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(['Botanical Name','Expected Common Name','Wikipedia Page link','Image urls'])
# %%
# fetch wikipedia data
with open('plant_botanical_names.txt','r') as file:
    for line in file:
        plantName = line.replace("\n", "")
        print(str(plantName))
# %%
        try:
            pageObject = wikipedia.page(plantName)
            pageHtml = wikipedia.page(plantName).html()
            with open('wikipedia_pages_by_plant_botanical_names.csv','a') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow([plantName,pageObject.title,pageObject.url," ".join(str(x) for x in pageObject.images)])
        except:
            #if a "PageError" was raised, ignore it and continue to next link
            with open('wikipedia_pages_by_plant_botanical_names.csv','a') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow([plantName,'not found','not found','not found'])
            print('##### not found #####')
            continue
