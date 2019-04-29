import os, json, numpy, src, re

class SentimentCalculator(object):

    def __init__(self, lexicons):
        items = []

        for file_name in lexicons:
            with open(src.getAbsoluteFilePath(f'../lexicons/{file_name}'), 'r') as f:
                for l in f:
                    items.append(tuple(l.rstrip('\n').split('\t')))

                f.close()

        self.sentiment_scores = dict(items)

    def calculate(self, tweetFileName, outputFileName = 'sentiment_scores.txt'):
        rf, of = src.getFiles(tweetFileName, outputFileName)
        o_str = ""

        for line in rf:
            sentiment_score = numpy.sum([int(self.sentiment_scores.get(src.generalizeTerm(word), 0)) for word in json.loads(line)['text'].split()])

            o_str += str(sentiment_score) + '\n'

        of.write(o_str)

        rf.close()
        of.close()
