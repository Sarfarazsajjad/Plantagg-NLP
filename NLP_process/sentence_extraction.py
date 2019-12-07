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
import re

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
                    # filterdSentence = tokenizer.tokenize(sentenceThatContainHeightKeyword)
                    # sentenceThatContainHeightKeyword = " ".join(str(x) for x in filterdSentence)
                    # print("plant Name is :" ,plantName, sentenceThatContainHeightKeyword);
                    doc = nlp(sentenceThatContainHeightKeyword)
                    count = 0
                    plant_height_data = []
                    for token in doc:
                        t = token.text
                        if t == 'm' or t == 'meter' or t == 'metre' or t == 'ft' or t == 'foot' or t == 'cm' or t =='centimetre' or t == 'in':
                            # if len(doc) > (token.i+1):
                                # next_token = doc[token.i + 1]
                            prev_token = doc[token.i - 1]
                            if prev_token.like_num:
                                count += 1
                                # print("token",token," token.i",token.i," len(doc)",len(doc))
                                token_sentence = doc[prev_token.i: token.i + 1]
                                print("case#1",chalk.yellow.bold(token_sentence))
                                plant_height_data.append(token_sentence)
                                if doc[prev_token.i - 2].like_num: # 1 to 2 unit
                                    count += 1
                                    token_sentence = doc[prev_token.i - 2: token.i + 1]
                                    print("case#2",chalk.blue.bold(token_sentence))
                                    plant_height_data.append(token_sentence)
                                else:
                                    pass
                            else: #get data for case#3 x-x unit
                                if prev_token.is_punct == False:
                                    token_sentence = doc[prev_token.i: token.i + 1]
                                    print("case#3",chalk.magenta(token_sentence)) #x-x uni
                                    plant_height_data.append(token_sentence)
                                else:
                                    pass # do nothing if theres a punct mark
                                
                                # if next_token.lower_ == "m" or next_token.lower_ == 'ft' or next_token.lower_ == 'meter' or next_token.lower_ == 'metre' or next_token.lower_ == 'cm' or next_token.lower_ == 'in' or next_token.lower_ == 'foot':
                                # count += 1
                                # token_sentence = doc[prev_token.i:next_token.i + 1]
                                # print('Height sentence',token_sentence)
                                # unit = token_sentence[len(token_sentence) - 1:len(token_sentence)]
                                # print(unit)
                                # writer.writerow([plantName,category,unit,'',token_sentence,'',wikiLink,sentenceThatContainHeightKeyword,''])
                        
                    # unit cleanup
                    plant_height_data_str = []
                    plant_height_data_str_ft = ''
                    plant_height_data_str_cm = ''
                    plant_height_data_str_m = ''
                    plant_height_data_str_in = ''
                    for valueWithUnit in plant_height_data:
                        stringData = valueWithUnit.text
                        stringData = stringData.replace("-"," ")
                        stringData = stringData.replace("centimetre","cm")
                        stringData = stringData.replace("foot","ft")
                        stringData = stringData.replace("meter","m")
                        stringData = stringData.replace("inch","in")
                        stringData = stringData.replace('–', ' ')
                        stringData = stringData.replace('to', ' ')
                        stringData = stringData.replace(',', '')
                        stringData = stringData.replace('1/2', '0.5')
                        
                        if stringData.find('in') > 0:
                            plant_height_data_str_in = plant_height_data_str_in + stringData
                            plant_height_data_str_in = plant_height_data_str_in.replace('in','')
                        if stringData.find('ft') > 0:
                            plant_height_data_str_ft = plant_height_data_str_ft + stringData
                            plant_height_data_str_ft = plant_height_data_str_ft.replace('ft','')
                        if stringData.find(' m') > 0:
                            plant_height_data_str_m = plant_height_data_str_m + stringData
                            plant_height_data_str_m = plant_height_data_str_m.replace('m','')
                        if stringData.find(' cm') > 0:
                            plant_height_data_str_cm = plant_height_data_str_cm + stringData
                            plant_height_data_str_cm = plant_height_data_str_cm.replace('cm','')
                        
                        plant_height_data_str.append(stringData)
                        
                    
                    print(chalk.red(plantName),plant_height_data)
                    print(chalk.green(plantName),plant_height_data_str)

                    # inch
                    # remove all characters
                    plant_height_data_str_in = removeAlphabets(plant_height_data_str_in)
                    print(chalk.yellow(plantName),'inch values',plant_height_data_str_in)
                    plant_height_data_str_in = plant_height_data_str_in.split()
                    try:
                        plant_height_data_str_in = list(map(float, plant_height_data_str_in))
                        plant_height_data_str_in = sorted(plant_height_data_str_in)
                        print(chalk.cyan.bold(plantName),'inch values',plant_height_data_str_in)
                    except ValueError:
                        pass

                    # ft
                    plant_height_data_str_ft = removeAlphabets(plant_height_data_str_ft)
                    print(chalk.yellow(plantName),'ft values',plant_height_data_str_ft)
                    plant_height_data_str_ft = plant_height_data_str_ft.split()
                    try:
                        plant_height_data_str_ft = list(map(float, plant_height_data_str_ft))
                        plant_height_data_str_ft = sorted(plant_height_data_str_ft)
                        print(chalk.cyan.bold(plantName),'ft values',plant_height_data_str_ft)
                    except ValueError:
                        pass
                    # m
                    plant_height_data_str_m = removeAlphabets(plant_height_data_str_m)
                    print(chalk.yellow(plantName),'m values',plant_height_data_str_m)
                    plant_height_data_str_m = plant_height_data_str_m.split()
                    try:
                        plant_height_data_str_m = list(map(float, plant_height_data_str_m))
                        plant_height_data_str_m = sorted(plant_height_data_str_m)
                        print(chalk.cyan.bold(plantName),'m values',plant_height_data_str_m)
                    except ValueError:
                        pass

                    # cm
                    plant_height_data_str_cm = removeAlphabets(plant_height_data_str_cm)
                    print(chalk.yellow(plantName),'cm values',plant_height_data_str_cm)
                    plant_height_data_str_cm = plant_height_data_str_cm.split()
                    try:
                        plant_height_data_str_cm = list(map(float, plant_height_data_str_cm))
                        plant_height_data_str_cm = sorted(plant_height_data_str_cm)
                        print(chalk.cyan.bold(plantName),'cm values',plant_height_data_str_cm)
                    except ValueError:
                        pass


                    if (len(plant_height_data_str_in) > 0):
                        temp = ['x'] * 10
                        for index,value in enumerate(plant_height_data_str_in):
                            temp[index] = value
                        
                        writer.writerow([plantName,category,'in',temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],wikiLink,sentenceThatContainHeightKeyword])
                    
                    if (len(plant_height_data_str_cm) > 0):
                        temp = ['x'] * 10
                        for index,value in enumerate(plant_height_data_str_cm):
                            temp[index] = value
                        
                        writer.writerow([plantName,category,'cm',temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],wikiLink,sentenceThatContainHeightKeyword])
                    
                    if (len(plant_height_data_str_ft) > 0):
                        temp = ['x'] * 10
                        for index,value in enumerate(plant_height_data_str_ft):
                            temp[index] = value

                        writer.writerow([plantName,category,'ft',temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],wikiLink,sentenceThatContainHeightKeyword])
                    
                    if (len(plant_height_data_str_m) > 0):
                        temp = ['x'] * 10
                        for index,value in enumerate(plant_height_data_str_m):
                            temp[index] = value

                        writer.writerow([plantName,category,'m',temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],wikiLink,sentenceThatContainHeightKeyword])
                
                
                    # if (count > 0):
                        # print(count,chalk.red.bold('tokens found in'),plantName,'\n')
                    # else:
                        # writer.writerow([plantName,category,'not found','','not found','',wikiLink,sentenceThatContainHeightKeyword,''])
                        # print(count,chalk.red('tokens matched in'),plantName,'\n')

    if(foundHeight == False):
        print(chalk.red("No Height for "),plantName)   
        with open('plantHeightData.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([plantName,category,'x','x','x','x','x','x','x','x','x','x','x',wikiLink,'x'])           

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
    with open('plantSoilphData.csv','a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        for sentence in lemmatizedSentences:
            for word in sentence:
                if (word == 'ph' or word == 'pH' or word == 'PH'):
                    print(chalk.green.bold('Soil pH found for'),plantName)
                    soilPH = True
                    containsoilph = " ".join(str(x) for x in sentence)
                    # print(containsoilph,'\n')
                    # filterdSentence = tokenizer.tokenize(containsoilph)
                    # containsoilph = " ".join(str(x) for x in filterdSentence)
                    # print("plant Name is :" ,plantName, containsoilph);
                    doc = nlp(containsoilph)
                    count = 0
                    for token in doc:
                        if token.like_num:
                            next_token = doc[token.i + 1]
                            prev_token = doc[token.i - 1]
                            if prev_token.lower_ == "soil" or prev_token.lower_ == 'above' or prev_token.lower_ == 'below' or prev_token.lower_ == 'of' or prev_token.lower_ == 'level' or next_token.lower_ == 'level' or prev_token.lower_ == 'range' or prev_token.lower_ == 'about' or prev_token.lower_ == 'ph' or prev_token.lower_ == 'pH' or prev_token.lower_ == 'between':
                                count += 1
                                token_sentence = doc[prev_token.i:next_token.i + 1]
                                # print('Height sentence',token_sentence)
                                unit = token_sentence[len(token_sentence) - 1:len(token_sentence)]
                                # print(unit)
                                writer.writerow([plantName,category,unit,'',token_sentence,'',wikiLink,containsoilph,''])
                    
                    if (count > 0):
                        print(count,chalk.yellow('tokens found in'),plantName,'\n')
                    else:
                        writer.writerow([plantName,category,'not found','','not found','',wikiLink,containsoilph,''])
                        print(count,chalk.red('tokens matched in'),plantName,'\n')

    
    if(soilPH == False):
        print(chalk.red("No Soil pH for "),plantName)   
        with open('plantSoilphData.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([plantName,category,'not found','','not found','',wikiLink,''])

def removeAlphabets(str):
    result = str.replace('a','')
    result = result.replace('b','')
    result = result.replace('c','')
    result = result.replace('d','')
    result = result.replace('e','')
    result = result.replace('f','')
    result = result.replace('g','')
    result = result.replace('h','')
    result = result.replace('i','')
    result = result.replace('j','')
    result = result.replace('k','')
    result = result.replace('l','')
    result = result.replace('m','')
    result = result.replace('n','')
    result = result.replace('o','')
    result = result.replace('p','')
    result = result.replace('q','')
    result = result.replace('r','')
    result = result.replace('s','')
    result = result.replace('t','')
    result = result.replace('u','')
    result = result.replace('v','')
    result = result.replace('w','')
    result = result.replace('x','')
    result = result.replace('y','')
    result = result.replace('z','')
    result = result.replace('A','')
    result = result.replace('B','')
    result = result.replace('C','')
    result = result.replace('D','')
    result = result.replace('E','')
    result = result.replace('F','')
    result = result.replace('G','')
    result = result.replace('H','')
    result = result.replace('I','')
    result = result.replace('J','')
    result = result.replace('K','')
    result = result.replace('L','')
    result = result.replace('M','')
    result = result.replace('N','')
    result = result.replace('O','')
    result = result.replace('P','')
    result = result.replace('Q','')
    result = result.replace('R','')
    result = result.replace('S','')
    result = result.replace('T','')
    result = result.replace('U','')
    result = result.replace('V','')
    result = result.replace('W','')
    result = result.replace('X','')
    result = result.replace('Y','')
    result = result.replace('Z','')
    return result

def clearFiles():
    with open('plantHeightData.csv','w+',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Plantname","Category","Unit","Value 1","Value 2","Value 3","Value 4","Value 5","Value 6","Value 7","Value 8","Value 9","Value 10","Wiki link","Evidence (Source text/Sentence)"])

    # with open('plantSunlightData.csv','w+',newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(["Plantname","Category", "Unit",'Unit Verified',"Value",'Value Verified',"Wiki link","Evidence (Source text/Sentence)"])

    # with open('plantWaterData.csv','w+',newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(["Plantname","Category", "Unit",'Unit Verified',"Value",'Value Verified',"Wiki link","Evidence (Source text/Sentence)"])

    # with open('plantSoilData.csv','w+',newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(["Plantname","Category", "Unit",'Unit Verified',"Value",'Value Verified',"Wiki link","Evidence (Source text/Sentence)"])

    # with open('plantSoilphData.csv','w+',newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(["Plantname","Category", "Unit",'Unit Verified',"Value",'Value Verified',"Wiki link","Evidence (Source text/Sentence)"])

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

            # findSunlightWordInSentences(lemmatizedSentences,plantName,category,wikiLink)

            # findWaterWordInSentences(lemmatizedSentences,plantName,category,wikiLink)

            # findSoilWordInSentences(lemmatizedSentences,plantName,category,wikiLink)

            # findSoilphWordInSentences(lemmatizedSentences,plantName,category,wikiLink)
