import tweepy
import json
import os

class FileLogStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print('New status added to file!')
        file = open(os.path.join(os.path.dirname(__file__), '../out/output.txt'), 'a')
        file.write(json.dumps(status._json) + '\n')
