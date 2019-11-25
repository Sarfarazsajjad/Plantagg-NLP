import nltk
print('NTLK version: %s' % (nltk.__version__))
from nltk import word_tokenize, pos_tag, ne_chunk
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')

article = '''
Asian shares skidded on Tuesday after a rout in tech stocks put Wall Street to the sword, while a 
sharp drop in oil prices and political risks in Europe pushed the dollar to 16-month highs as investors dumped 
riskier assets. MSCI’s broadest index of Asia-Pacific shares outside Japan dropped 1.7 percent to a 1-1/2 
week trough, with Australian shares sinking 1.6 percent. Japan’s Nikkei dived 3.1 percent led by losses in 
electric machinery makers and suppliers of Apple’s iphone parts. Sterling fell to $1.286 after three straight 
sessions of losses took it to the lowest since Nov.1 as there were still considerable unresolved issues with the
European Union over Brexit, British Prime Minister Theresa May said on Monday.'''

import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint

nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')

print('NTLK version: %s' % (nltk.__version__))

def fn_preprocess(art):
    art = nltk.word_tokenize(art)
    art = nltk.pos_tag(art)
    return art

art_processed = fn_preprocess(article)

results = ne_chunk(art_processed)

# for x in str(results).split('\n'):
#     if '/NN' in x:
#         print(x)
        
pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(art_processed)
# print(cs)

iob_tagged = tree2conlltags(cs)
# pprint(iob_tagged)


namedEntities = []
for word, pos, ner in iob_tagged:
    namedEntities.append(ner)
#     print(word, pos, ner)

print('Named Entites in Document')
print(len(namedEntities))
