import wikipedia as wikipedia
import nltk as nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import csv
import os

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
                print("plant Name is :" ,plantName, sentenceThatContainHeightKeyword);
                with open('plantData.csv','a',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([plantName,sentenceThatContainHeightKeyword,""])

def findSunlightWordInSentences(lemmatizedSentences,plantName):
    for sentence in lemmatizedSentences:
        for word in sentence:
            if (word == 'sun' or word =='sunlight'):
                containsunlight = " ".join(str(x) for x in sentence)
                print("Plant:" ,plantName, "sentence",containsunlight);
                with open('plantSunlightData.csv','a',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([plantName,containsunlight,""])

def clearFile():
    with open('plantData.csv','w+',newline='') as csvfile:
        pass

    with open('plantSunlightData.csv','w+',newline='') as csvfile:
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

        findSunlightWordInSentences(lemmatizedSentences,plantName)
