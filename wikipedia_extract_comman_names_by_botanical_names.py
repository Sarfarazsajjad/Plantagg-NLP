# %%
import wikipedia as wikipedia
import csv
# %%
# prepare csv header
with open('wikipedia_pages_by_plant_botanical_names.csv','a') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(['Botanical Name','Expected Common Name','Wikipedia Page link','Image urls'])

with open('plant_botanical_names.txt','r') as file:
    for line in file:
        print(line)
# %%
        pageObject = wikipedia.page(line)
        pageHtml = wikipedia.page(line).html()
        with open('wikipedia_pages_by_plant_botanical_names.csv','a') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow([line.replace("\n", ""),pageObject.title,pageObject.url," ".join(str(x) for x in pageObject.images)])


# %%
