import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk import ne_chunk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint

# nlp = spacy.load("en_core_web_sm")
ex1 = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'
ex = 'A rose is a woody perennial flowering plant of the genus Rosa in the family Rosaceae or the flower it bears. There are over three hundred species and thousands of cultivars. They form a group of plants that can be erect shrubs climbing or trailing with stems that are often armed with sharp prickles. Flowers vary in size and shape and are usually large and showy in colours ranging from white through yellows and reds. Most species are native to Asia with smaller numbers native to Europe North America and northwestern Africa. Species cultivars and hybrids are all widely grown for their beauty and often are fragrant. Roses have acquired cultural significance in many societies. Rose plants range in size from compact miniature roses to climbers that can reach seven meters in height. Different species hybridize easily and this has been used in the development of the wide range of garden roses.'

# Tokenize words from the sentence
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent  = preprocess(ex)

print(sent)

pattern = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)

iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

ne_tree = ne_chunk(pos_tag(word_tokenize(ex)))
print(ne_tree)