import os, json, src, operator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class TermFrequencyCalculator(object):

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def calculate(self, tweetFileName, outputFileName="term_frequency.txt"):
        rf, of = src.getFiles(tweetFileName, outputFileName)

        terms = {}

        for line in rf:
            for w in word_tokenize(json.loads(line)['text'].lower()):
                word = src.generalizeTerm(w)

                if not word in self.stop_words:
                    if word in terms:
                        terms[word] = terms[word] + 1
                    else:
                        terms[word] = 1

        for word, freq in sorted(terms.items(), key=operator.itemgetter(1), reverse=True):
            print(word + "\t → " + str(freq))
