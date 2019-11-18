import spacy
from spacy.lang.en import STOP_WORDS
# import en_core_web_sm
nlp = spacy.load("en_core_web_md")


# NLP process goes the following way
# 1. tokenize the text
# 2. remove stop words
# 3. convert the text to root words (normailze the text)
# 4. Parts of speech tagging
# 4. Do more stuff (work in progress)

text = "This is a cat who's height is 10m is partying!."

doc = nlp(text)

token_list = []

for token in doc:
  token_list.append(token)

filtered_sentence =[] 

# for word in doc:
#     lexeme = nlp.vocab[word]
#     if lexeme.is_stop == False:
#         filtered_sentence.append(word)

# print(type(nlp))
# print(filtered_sentence)


# Finding root words 

lemma_word1 = [] 
for token in doc:
    lemma_word1.append(token.lemma_)


print(lemma_word1)