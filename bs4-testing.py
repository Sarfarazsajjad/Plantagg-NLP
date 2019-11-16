# import libraries
import urllib3
from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

# specify the url
wiki_page = "https://en.wikipedia.org/wiki/abelia_grandiflora"
# "https://en.wikipedia.org/wiki/Acer_palmatum",
# "https://en.wikipedia.org/wiki/Aesculus_pavia",
# "https://en.wikipedia.org/wiki/Linnaea_x_grandiflora"
# ]  

# query the website and return the html to the variable ‘page’
response = http.request('GET', wiki_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(response.data,features="html.parser")
print(soup.prettify())

# all_string = soup.get_text()

# print(soup.get_text())
# paragraph = ' '.join(map(lambda p:p.text,soup.find_all('p')))
# paragraph.encode('ascii',errors='replace').replace("?"," ")
# print(paragraph)

# for items in paragraph:
#     print(items.text)
# print(type(soup.get_text()))
# print(paragraph[1])

# print(string)
# soup1 = BeautifulSoup(paragraph,features="html.parser")
# print(soup1.prettify())

# plant_name = soup.find('h1', attrs={'class': 'firstHeading','id': 'firstHeading'})

# content = soup.find('p')

# name = plant_name.text.strip() # strip() is used to remove starting and trailing
# page_content = content.text.strip()
# print(name)
# print(content)


# html = "<p>The plant is 10m <strong>tall</strong></p>"
# invalid_tags = ['b', 'i', 'u','p','strong']
# soup2 = BeautifulSoup(html)
# for tag in invalid_tags: 
#     for match in soup2.findAll(tag):
#         match.replaceWithChildren()
# print(soup2)