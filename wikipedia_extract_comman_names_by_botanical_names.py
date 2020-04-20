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
        line = file.readline()
        plantName = line.replace("\n", "")
        print(str(plantName))
        try:
            pageObject = wikipedia.page(plantName)
            pageHtml = wikipedia.page(plantName).html()
            soup = BeautifulSoup(pageHtml)
            common_names_string = extract_common_names(soup)
            print('common names: ' + common_names_string)
            
            with open('wikipedia_plant_common_name_by_botanical_names.csv','a') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow([plantName,pageObject.title,common_names_string,pageObject.url," ".join(str(x) for x in pageObject.images)])
        except:
            #if a "PageError" was raised, ignore it and continue to next link
            with open('wikipedia_plant_common_name_by_botanical_names.csv','a') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow([plantName,'not found','not found','not found','not found'])
            print('##### not found #####')
            continue
# %%
def extract_common_names(soup):
    all_p_tags = soup.find_all('p')
    print(len(all_p_tags))
    b_tags = []
    for p in all_p_tags:
        b_tags_in_p = p.find_all('b')
        for tag in b_tags_in_p:
            b_tags.append(tag)

    if (len(b_tags)):
        print(b_tags)

    common_names = []
    for b_tag in b_tags:
        common_names.append(b_tag.string)

    print(common_names)

    common_names_iterator = iter(common_names)
    common_names_string = next(common_names_iterator)
    for common_name in common_names_iterator:
        common_names_string = common_names_string + '; ' + common_name

    # print(common_names_string)

    return common_names_string
