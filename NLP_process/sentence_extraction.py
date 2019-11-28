import wikipedia as wikipedia
import nltk as nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import csv
import os
import spacy
import en_core_web_md
nlp = en_core_web_md.load()
from simple_chalk import chalk
from nltk.tokenize import RegexpTokenizer

# Regix to filter data from text
tokenizer = RegexpTokenizer(r'\w+')

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


def findHeightWordInSentences(lemmatizedSentences,plantName,category,wikiLink):
    foundHeight = False
    with open('plantHeightData.csv','a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for sentence in lemmatizedSentences:
            for word in sentence:
                if (word == 'height' or word == 'tall'):
                    print(chalk.green.bold('height found for'),plantName)
                    foundHeight = True
                    sentenceThatContainHeightKeyword = " ".join(str(x) for x in sentence)
                    # print(sentenceThatContainHeightKeyword,'\n')
                    filterdSentence = tokenizer.tokenize(sentenceThatContainHeightKeyword)
                    sentenceThatContainHeightKeyword = " ".join(str(x) for x in filterdSentence)
                    # print("plant Name is :" ,plantName, sentenceThatContainHeightKeyword);
                    doc = nlp(sentenceThatContainHeightKeyword)
                    count = 0
                    for token in doc:
                        if token.like_num:
                            next_token = doc[token.i + 1]
                            prev_token = doc[token.i - 2]
                            if next_token.lower_ == "m" or next_token.lower_ == 'ft' or next_token.lower_ == 'meter' or next_token.lower_ == 'metre' or next_token.lower_ == 'cm' or next_token.lower_ == 'in' or next_token.lower_ == 'foot':
                                count += 1
                                token_sentence = doc[prev_token.i:next_token.i + 1]
                                # print('Height sentence',token_sentence)
                                unit = token_sentence[len(token_sentence) - 1:len(token_sentence)]
                                # print(unit)
                                writer.writerow([plantName,category,unit,'',token_sentence,'',wikiLink,sentenceThatContainHeightKeyword,''])
                    
                    if (count > 0):
                        print(count,chalk.yellow('tokens found in'),plantName,'\n')
                    else:
                        writer.writerow([plantName,category,'not found','','not found','',wikiLink,sentenceThatContainHeightKeyword,''])
                        print(count,chalk.red('tokens matched in'),plantName,'\n')

    
    if(foundHeight == False):
        print(chalk.red("No Height for "),plantName)   
        with open('plantHeightData.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([plantName,category,'not found','','not found','',wikiLink,''])           

def findSunlightWordInSentences(lemmatizedSentences,plantName,category,wikiLink):
    sunlightFound = False
    with open('plantSunlightData.csv','a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for sentence in lemmatizedSentences:
            for word in sentence:
                if (word == 'sun' or word =='sunlight' or word == 'sunny'):
                    sunlightFound = True
                    print('Sunglight found in',plantName)
                    containsunlight = " ".join(str(x) for x in sentence)
                    filterdSentence = tokenizer.tokenize(containsunlight)
                    containsunlight = " ".join(str(x) for x in filterdSentence)
                    # print("Plant:" ,plantName, "sentence",containsunlight);
                    doc = nlp(containsunlight)
                    count = 0
                    for token in doc:
                        if (token.lower_ == 'sun' or token.lower_ == 'sunny' or token.lower_ == 'sunlight' or token.lower_ == 'sun s ray' or token.lower_ == 'shade'):
                            count += 1
                            pre_token = doc[token.i - 1]
                            value = doc[pre_token.i:token.i + 1]
                            writer.writerow([plantName,category,'','',value,'',wikiLink,containsunlight,''])

                    if (count > 0):
                        print(count,chalk.yellow('sunlight tokens found in'),plantName,'\n')
                    else:
                        writer.writerow([plantName,category,'not found','','not found','',wikiLink,containsunlight,''])
                        print(count,chalk.red('sunlight tokens matched in'),plantName,'\n')

    if(sunlightFound == False):
        with open('plantSunlightData.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([plantName,category,'','','','',wikiLink,'']) 

def findWaterWordInSentences(lemmatizedSentences,plantName,category,wikiLink):
    waterFound = False
    with open('plantWaterData.csv','a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for sentence in lemmatizedSentences:
            for word in sentence:
                if (word == 'water' or word =='Water' or word == 'waterlogged' or word == 'wet' or word == 'damp'):
                    waterFound = True
                    print('water found for ',plantName)
                    containwater = " ".join(str(x) for x in sentence)
                    filterdSentence = tokenizer.tokenize(containwater)
                    containwater = " ".join(str(x) for x in filterdSentence)
                    # print("Plant:" ,plantName, "sentence",containwater);
                    doc = nlp(containwater)
                    count = 0
                    for token in doc:
                        if (token.lower_ == 'water' or token.lower_ == 'wet' or token.lower_ == 'damp' or token.lower_ == 'soggy' or token.lower_ == 'moisture'):
                            count +=1
                            pre_token = doc[token.i - 3]
                            value = doc[pre_token.i:token.i + 1]
                            writer.writerow([plantName,category,'','',value,'',wikiLink,containwater,''])
    
                    if (count > 0):
                        print(count,chalk.magenta('water tokens in'),plantName,'\n')
                    else:
                        writer.writerow([plantName,category,'','','','',wikiLink,containwater,''])
                        print(count,chalk.red('water tokens matched in'),plantName,'\n')

    if(waterFound == False):
        with open('plantWaterData.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([plantName,category,'','','','',wikiLink,'']) 

def findSoilWordInSentences(lemmatizedSentences,plantName,category,wikiLink):
    soilFound = False
    for sentence in lemmatizedSentences:
        for word in sentence:
            if (word == 'soil' or word == 'earth' or word == 'dirt' or word == 'clay' or word == 'ground'):
                soilFound = True
                print('soil found for ',plantName)
                containsoil = " ".join(str(x) for x in sentence)
                # print("Plant:" ,plantName, "sentence",containsoil);
                with open('plantSoilData.csv','a',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([plantName,category,'','','','',wikiLink,containsoil,""])

    if(soilFound == False):
        with open('plantSoilData.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([plantName,category,'','','','',wikiLink,''])

def findSoilphWordInSentences(lemmatizedSentences,plantName,category,wikiLink):
    soilPH = False
    for sentence in lemmatizedSentences:
        for word in sentence:
            if (word == 'ph' or word == 'pH' or word == 'PH'):
                soilPH = True
                print('soilPH found for ',plantName)
                containsoilph = " ".join(str(x) for x in sentence)
                # print("Plant:" ,plantName, "sentence",containsoilph);
                with open('plantSoilphData.csv','a',newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([plantName,category,'','','','',wikiLink,containsoilph,""])

    if(soilPH == False):
        with open('plantSoilphData.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([plantName,category,'','','','',wikiLink,''])

def clearFiles():
    with open('plantHeightData.csv','w+',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Plantname","Category", "Unit",'Unit Verified',"Value",'Value Verified',"Wiki link","Evidence (Source text/Sentence)"])

    with open('plantSunlightData.csv','w+',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Plantname","Category", "Unit",'Unit Verified',"Value",'Value Verified',"Wiki link","Evidence (Source text/Sentence)"])

    with open('plantWaterData.csv','w+',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Plantname","Category", "Unit",'Unit Verified',"Value",'Value Verified',"Wiki link","Evidence (Source text/Sentence)"])

    with open('plantSoilData.csv','w+',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Plantname","Category", "Unit",'Unit Verified',"Value",'Value Verified',"Wiki link","Evidence (Source text/Sentence)"])

    with open('plantSoilphData.csv','w+',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Plantname","Category", "Unit",'Unit Verified',"Value",'Value Verified',"Wiki link","Evidence (Source text/Sentence)"])

if __name__ == '__main__':

    clearFiles()
    with open('plantData.csv') as csvfile:
        next(csvfile)
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            plantName = row[1]
            category = row[2]
            wikiLink = row[3]
            plantPageData = row[4]
            # page = getPage(plantName);
            sents = sentenceTokenize(plantPageData)
            # print(sents)

            lemmatizedSentences = lemmitizedList(sents);
            # print(lemmatizedSentences)

            findHeightWordInSentences(lemmatizedSentences,plantName,category,wikiLink)

            findSunlightWordInSentences(lemmatizedSentences,plantName,category,wikiLink)

            findWaterWordInSentences(lemmatizedSentences,plantName,category,wikiLink)

            findSoilWordInSentences(lemmatizedSentences,plantName,category,wikiLink)

            findSoilphWordInSentences(lemmatizedSentences,plantName,category,wikiLink)
