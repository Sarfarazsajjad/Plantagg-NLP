import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import re


# doc = nlp('A rose is a woody perennial flowering plant of the genus Rosa in the family Rosaceae or the flower it bears. There are over three hundred species and thousands of cultivars. They form a group of plants that can be erect shrubs climbing or trailing with stems that are often armed with sharp prickles. Flowers vary in size and shape and are usually large and showy in colours ranging from white through yellows and reds. Most species are native to Asia with smaller numbers native to Europe North America and northwestern Africa. Species cultivars and hybrids are all widely grown for their beauty and often are fragrant. Roses have acquired cultural significance in many societies. Rose plants range in size from compact miniature roses to climbers that can reach seven meters in height. Different species hybridize easily and this has been used in the development of the wide range of garden roses.')

# doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
# pprint([(X.text, X.label_) for X in doc.ents])
# pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))

ny_bb = url_to_string('https://en.wikipedia.org/wiki/Rose')
article = nlp(ny_bb)
print(len(article.ents))

labels = [x.label_ for x in article.ents]
print(Counter(labels))


items = [x.text for x in article.ents]
print(Counter(items).most_common(3))

sentences = [x for x in article.sents]
print(sentences[20])

[(x.orth_,x.pos_, x.lemma_) for x in [y for y in nlp(str(sentences[20])) if not y.is_stop and y.pos_ != 'PUNCT']]

dict([(str(x), x.label_) for x in nlp(str(sentences[20])).ents])

print([(x, x.ent_iob_, x.ent_type_) for x in sentences[20]])