## Import the English language class
from spacy.lang.en import English

# from Acer_palmatum import *

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/huzaifajalali/Documents/Pythondev/Plantagg-NLP/wiki-plant-data')  
# from Acer_palmatum import Acer_palmatum_text
# from Bouteloua_dactyloides import Bouteloua_dactyloides_text
from corpus import *


## Create the nlp object
nlp = English()


## Created by processing a string of text with the nlp object
doc = nlp(Bouteloua_dactyloides_text)


for token in doc:
    if token.like_num:
        next_token = doc[token.i + 1]
        if next_token.text == "m" or next_token.text == 'ft' or next_token.text == 'meters' or next_token.text == 'cm':
            print('Height found',token.text)