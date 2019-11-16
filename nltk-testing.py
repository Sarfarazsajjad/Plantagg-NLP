from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.collocations import BigramAssocMeasures,BigramCollocationFinder,TrigramAssocMeasures, TrigramCollocationFinder



sent = """
Linnaea × grandiflora, synonym Abelia × grandiflora, is a hybrid Linnaea, raised by hybridising 
L. chinensis with L. uniflora. It is a deciduous or semievergreen multistemmed shrub with rounded, 
spreading, or gracefully arching branches to 1.0-1.8 m tall. The leaves are ovate, glossy, dark green, 
and 2–6 cm long. The flowers are produced in clusters, white, tinged pink, bell-shaped, to 2 cm long. 
Unlike most flowering shrubs in cultivation, the species blooms from late summer to well into the autumn.
The Latin specific epithet grandiflora means "abundant flowers".[2] Linnaea × grandiflora was first raised in 1886 at the Rovelli nursery at Pallanza 
(now Verbania), on Lake Maggiore in Italy. It is used as an ornamental plant in specimen plantings in gardens, 
or in a mixed border with other shrubs. Propagation is by cuttings. Though relatively easy to cultivate, 
it is not fully hardy, and requires a sheltered position in full sun. This plant is still widely listed 
in the UK under the name Abelia. The variegated cultivar 'Hopleys’,[3] with pale pink flowers and growing 
to 1.5m × 1.5m, has gained the Royal Horticultural Society's Award of Garden Merit."""

tokens = sent_tokenize(sent)
# print(len(tokens))


# stemming


# passing in each token that is a sentence from a collection of sentences 
# and then breaking that sentence into individual words
words = [word_tokenize(token) for token in tokens]
# print(type(words))
# print(type(word_tokenize(sent)))
# print(words)


customStopWordList = ['×','``','’','`','\'\'']
# now we need to remove the stopwords that dont have any meaning in the sentence meaning
customStopWords = set(stopwords.words('english')+list(punctuation)+customStopWordList)
# print(customStopWords)


wordsFilter = [word for word in word_tokenize(sent) if word not in customStopWords]
# print(wordsFilter)


# how to identify meaning from context

# now forming bigrams to find relation of occurance b/w words
bigram_measures = BigramAssocMeasures()
trigram_measures = TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordsFilter)
# triFinder = TrigramCollocationFinder.from_words(tokens)
wordRelations = sorted(finder.ngram_fd.items())
# triWordRelations = sorted(triFinder.ngram_fd.items())
for relation in wordRelations:
    print(relation)

# for triRelation in triWordRelations:
#     print(triRelation)

# stemming part of the text to the root word


