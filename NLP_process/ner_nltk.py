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
def fn_preprocess(art):
    art = nltk.word_tokenize(art)
    art = nltk.pos_tag(art)
    return art
art_processed = fn_preprocess(article)

# parts of speech tags done
print(art_processed)

# Text chunking is also called as shallow parsing which typically follows POS tagging to add more structure to the sentence. The result is grouping of words in “chunks”.
# So, lets perform chunking to our article which we have already POS tagged.
results = ne_chunk(art_processed)
for x in str(results).split('\n'):
    if '/NN' in x:
        print(x)