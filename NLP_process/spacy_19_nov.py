## Import the English language class
from spacy.lang.en import English

Callicarpa_Americana_text = '''
Callicarpa americana, the American beautyberry, is an open-habit, 
native shrub of the Southern United States which is often grown as an ornamental in gardens and yards. 
American beautyberries produce large clusters of purple berries,
which birds and deer eat, thus distributing the seeds.

The raw berries, while palatably sweet, are suitable for human consumption only in small amounts, because they are astringent. Some people have reported mild stomach cramps after consumption. The berries are also used in jellies and wine. The roots are used to make herbal tea. As a folk remedy it has been claimed that "fresh, crushed leaves of American beautyberry, Callicarpa americana ... helped keep biting insects away from animals such as horses and mules".[1] A chemical compound isolated from the plant, callicarpenal, was effective as a mosquito repellent in a laboratory experiment using a simulated skin model.[2
The native range of C. americana extends from Maryland to Florida, west to Texas and Arkansas, and also Mexico, Bermuda, the Bahamas and Cuba.[4]
Plants with white berries are found in cultivation under the name Callicarpa americana var. lactea; 4 [5][6] not all authorities recognize this as a distinct variety (in the sense of the botanical rank below subspecies).[7]
'''


japanese_mable_text = '''
Acer palmatum is a deciduous shrub or small tree reaching heights of 6 to 10 ft
(20 to 33 ft), rarely 16 metres (52 ft), often growing as an understory plant in shady woodlands'''

## Create the nlp object
nlp = English()

## Created by processing a string of text with the nlp object
doc = nlp(japanese_mable_text)

## Iterate over all the tokens in a Doc
# for token in doc:
#     print(token.text)

# # Get a specific section of the tokenzied document 
# span = doc[0:4]
# print(span.text)
# print(len(doc))
# print([token.like_num for token in doc])

for token in doc:
  if token.like_num:
    next_token = doc[token.i + 1]
    if next_token.text == "m" or next_token.text == 'ft' or next_token.text == 'meters':
      print('Height found',token.text)
