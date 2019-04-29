import os, json, src, operator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class TermFrequencyCalculator(object):

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def calculate(self, tweetFileName, outputFileName="term_frequency.txt"):
        rf, of = src.getFiles(tweetFileName, outputFileName)

        terms = {}
        term_count = 0
        o_str = ''

        for line in rf:
            tweet = json.loads(line)
            text = src.removeUrls(tweet['text'], tweet['entities']['urls'])

            for w in text.split():
                word = src.generalizeTerm(w)

                if word and not word in self.stop_words:
                    term_count += 1

                    if word in terms:
                        terms[word] = terms[word] + 1
                    else:
                        terms[word] = 1

        for word, freq in sorted(terms.items(), key=operator.itemgetter(1), reverse=True):
            o_str += word + "\t" + str(freq / term_count) + "\n"

        of.write(o_str)
