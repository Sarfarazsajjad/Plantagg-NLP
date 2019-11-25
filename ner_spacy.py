article = '''
Buxus sempervirens, the common box, European box, or boxwood,
is a species of flowering plant in the genus Buxus, native to western and southern Europe, 
northwest Africa, and southwest Asia, from southern England south to northern Morocco, 
and east through the northern Mediterranean region to Turkey. Buxus colchica of 
western Caucasus and B. hyrcana of northern Iran and eastern Caucasus are commonly treated as synonyms 
of B. sempervirens.'''

import spacy
import en_core_web_md
spacy_nlp = en_core_web_md.load()
doc = spacy_nlp(article)

token_list = []

# tokenize the content
for token in doc:
  token_list.append(token)

# lemmatize the content for root words
lemma_word1 = [] 
for token in doc:
    lemma_word1.append(token.lemma_)

print('Original Sentence: %s' % (article))

# for element in lemma_word1:
#   print('type %s' % (element))


# show named enties in the text
for element in doc.ents:
    print('Type: %s, Value: %s' % (element.label_, element))