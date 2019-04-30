import json, src, operator

class TopHashtagCalculator(object):

    def calculate(self, tweetFileName, outputFileName="top_hashtags.txt"):
        rf, of = src.getFiles(tweetFileName, outputFileName)

        hashtags = {}
        hashtag_count = 0
        o_str = ''

        for line in rf:
            tweet_hts = json.loads(line)['entities']['hashtags']

            for h in tweet_hts:
                hashtag = h['text'].lower()
                hashtag_count += 1

                if hashtag in hashtags:
                    hashtags[hashtag] = hashtags[hashtag] + 1
                else:
                    hashtags[hashtag] = 1

        print('--------------------------------------------------------------')
        print('The top 10 most used hashtags are:')
        print('\t')

        for i, ht in enumerate(sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)):
            hashtag, freq = ht
            o_str += hashtag + "\t" + str(freq / hashtag_count) + "\n"

            if i < 10:
                print(f'{i+1}. \t', hashtag)

        print('--------------------------------------------------------------')

        of.write(o_str)
