import wikipedia as wikipedia
import nltk as nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import csv
import os
import spacy
import en_core_web_md
nlp = en_core_web_md.load()

def getPage(plantName):
    return wikipedia.page(plantName).content  # get page data in string;


def wordTokenize(page):
    return nltk.word_tokenize(page)


def sentenceTokenize(sentencesArray):
    return nltk.sent_tokenize(sentencesArray)


def lemmitizedList(sents):
    lmtzr = WordNetLemmatizer()
    lemmatizedSentences = [[lmtzr.lemmatize(word) for word in nltk.word_tokenize(s)] for s in sents]
    return lemmatizedSentences


def findHeightWordInSentences(lemmatizedSentences,plantName):
    for sentence in lemmatizedSentences:
        for word in sentence:
            if (word == 'height' or word=='tall'):
                sentenceThatContainHeightKeyword = " ".join(str(x) for x in sentence)
                # print("plant Name is :" ,plantName, sentenceThatContainHeightKeyword);
                doc = nlp(sentenceThatContainHeightKeyword)
                for token in doc:
                    if token.like_num:
                        next_token = doc[token.i + 1]
                        prev_token = doc[token.i - 2]
                        if next_token.text == "m" or next_token.text == 'ft' or next_token.text == 'meter' or next_token.text == 'metre' or next_token.text == 'cm' and prev_token.like_num:
                            token_sentence = doc[prev_token.i:next_token.i + 1]
                            print('Height sentence',token_sentence)
                            unit = token_sentence[len(token_sentence) - 1:len(token_sentence)]
                            print(unit)
                            with open('plantHeightData.csv','a',newline='') as csvfile:
                                writer = csv.writer(csvfile)
                                writer.writerow([plantName,unit,'',token_sentence,'',sentenceThatContainHeightKeyword,""])

def findSunlightWordInSentences(lemmatizedSentences,plantName):
    for sentence in lemmatizedSentences:
        for word in sentence:
            if (word == 'sun' or word =='sunlight' or word == 'sunny'):
                containsunlight = " ".join(str(x) for x in sentence)
                print("Plant:" ,plantName, "sentence",containsunlight);
                with open('plantSunlightData.csv','a',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([plantName,containsunlight,""])

def findWaterWordInSentences(lemmatizedSentences,plantName):
    for sentence in lemmatizedSentences:
        for word in sentence:
            if (word == 'water' or word =='Water' or word == 'waterlogged' or word == 'wet' or word == 'damp'):
                containwater = " ".join(str(x) for x in sentence)
                print("Plant:" ,plantName, "sentence",containwater);
                with open('plantWaterData.csv','a',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([plantName,containwater,""])

def findSoilWordInSentences(lemmatizedSentences,plantName):
    for sentence in lemmatizedSentences:
        for word in sentence:
            if (word == 'soil' or word == 'earth' or word == 'dirt' or word == 'clay' or word == 'ground'):
                containsoil = " ".join(str(x) for x in sentence)
                print("Plant:" ,plantName, "sentence",containsoil);
                with open('plantSoilData.csv','a',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([plantName,containsoil,""])

def findSoilphWordInSentences(lemmatizedSentences,plantName):
    for sentence in lemmatizedSentences:
        for word in sentence:
            if (word == 'ph' or word == 'pH' or word == 'PH'):
                containsoilph = " ".join(str(x) for x in sentence)
                print("Plant:" ,plantName, "sentence",containsoilph);
                with open('plantSoilphData.csv','a',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([plantName,containsoilph,""])

def clearFile():
    with open('plantHeightData.csv','w+',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Plantname", "Unit",'Unit Verified',"Value",'Value Verified',"Sentence"])


    with open('plantSunlightData.csv','w+',newline='') as csvfile:
        pass

    with open('plantWaterData.csv','w+',newline='') as csvfile:
        pass

    with open('plantSoilData.csv','w+',newline='') as csvfile:
        pass

    with open('plantSoilphData.csv','w+',newline='') as csvfile:
        pass

if __name__ == '__main__':
    plantNames = ['Acer_palmatum', 'Anisacanthus_quadrifidus','buchloe_dactyloides','Callicarpa_americana','Cercis_canadensis','Chrysactinia_mexicana','Coreopsis_lanceolata','Cotinus_coggygria','Echinacea_paradoxa','Euphorbia_myrsinites','Hesperaloe_funifera','Hydrangea_quercifolia','juniperus_horizontalis','lantana_urticoides','Liriope_muscari','magnolia_soulangeana','Miscanthus_sinensis','Muhlenbergia_lindheimeri','Nerium','Opuntia_rufida','Phlox_divaricata','Phoenix_reclinata','Pyrus_calleryana','Rhododendron_japonicum','Rubus_idaeus','Salvia_guaranitica','Salvia_pachyphylla']
    singlePlant = ['Acer_palmatum','Anisacanthus_quadrifidus','buchloe_dactyloides']
    clearFile()
    
    for plantName in plantNames:
        page = getPage(plantName);

        sents = sentenceTokenize(page)
        # print(sents)

        lemmatizedSentences = lemmitizedList(sents);
        # print(lemmatizedSentences)

        findHeightWordInSentences(lemmatizedSentences,plantName)

        # findSunlightWordInSentences(lemmatizedSentences,plantName)

        # findWaterWordInSentences(lemmatizedSentences,plantName)

        # findSoilWordInSentences(lemmatizedSentences,plantName)

        # findSoilphWordInSentences(lemmatizedSentences,plantName)