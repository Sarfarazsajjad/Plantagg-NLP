# data from wikipedia
## Import the English language class
import spacy
import en_core_web_md

Echinacea_paradoxa_text = '''
Echinacea paradoxa, the yellow coneflower[2][3] or Bush's purple coneflower,[4] is a North American species of flowering plant in the sunflower family. It is native to southern Missouri, Arkansas, and south-central Oklahoma, with one isolated population reported from Montgomery County in eastern Texas.[5] It is listed as threatened in Arkansas.[4][6]

Echinacea paradoxa is a perennial herb up to 90 cm (3 feet) tall. One plant can produce several flower heads, each with white, pink, or yellow ray florets and pink or yellow disc florets.[6][7][8][9]

Varieties[1][6]
Echinacea paradoxa var. paradoxa - yellow rays - Arkansas and Missouri
Echinacea paradoxavar.neglecta - pink or white rays Oklahoma and Texas
Echinacea paradoxa var. paradoxa has a baseline chromosome number of x = 11, like most Echinacea plants.
'''

Lantana_urticoides_text = '''
Lantana urticoides, also known as West Indian shrubverbena,[3] 
Texas lantana or calico bush, is a three- to five-foot perennial 
shrub that grows in Mexico and the U.S. states of Texas,
Louisiana and Mississippi especially along the Gulf coast.
The plant can blossom from spring until the first frost.
It is a species of flowering plant within the verbena family, Verbenaceae.
'''


Salvia_guaranitica_text = '''
Salvia guaranitica, the anise-scented sage or hummingbird sage, 
is a species of Salvia native to a wide area of South America, including Brazil, 
Paraguay, Uruguay, and Argentina.
It is a perennial subshrub growing 4 to 5 ft (1.2 to 1.5 m) tall, 
spreading into a large patch through its spreading roots.
The leaves are ovate, 4 cm (1.6 in) long and nearly as wide,
with a fresh mint green color, and an anise scent when crushed. 
The inflorescences are up to 25 cm (9.8 in) long with flowers in various shades of blue, including an uncommonly true blue. In cold regions, flowering begins in mid summer and continues until frost.
Salvia guaranitica is a popular ornamental plant in mild areas.
It grows in either full or three quarter sunlight, in well-drained soil. Numerous cultivars have been selected, including 'Argentine Skies' (pale blue flowers), 'Black and Blue' (very dark violet blue calyx), 'Blue Ensign' (large blue flowers), and 'Purple Splendor' (Light purple flowers).[1] The cultivar 'Blue Enigma', with pure blue flowers, has gained the Royal Horticultural Society's Award of Garden Merit.
'''

## Create the nlp object
nlp = en_core_web_md.load()

## Process the text data , spacy automatically breaks text into tokens
doc = nlp(Salvia_guaranitica_text)

# lemmatize the data to get root words
lemmatized_docuemnt = [] 
for token in doc:
    lemmatized_docuemnt.append(token.lemma_)

## Iterate over all the tokens in a Doc
# for token in doc:
#     print(token.text)

# # Get a specific section of the tokenzied document 
# span = doc[0:4]
# print(span.text)
# print(len(doc))
# print([token.like_num for token in doc])


# show named enties in the text
# Uncomment to see the entities in the document
# for element in doc.ents:
#     print('Type: %s, Value: %s' % (element.label_, element))

# custom height extarction based on data review of pattern numeric value followed by m, ft,meters etc..
for token in doc:
  if token.like_num:
    next_token = doc[token.i + 1]
    if next_token.text == "m" or next_token.text == 'ft' or next_token.text == 'meters':
      print('Height found',token.text)
