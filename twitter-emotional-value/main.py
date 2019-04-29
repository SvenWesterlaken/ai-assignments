import tweepy
import auth as credentials
import nltk
from src import FileLogStreamListener, SentimentCalculator, TermFrequencyCalculator, HappiestOriginCalculator

auth = tweepy.OAuthHandler(credentials.api_key, credentials.api_key_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
nltk.download('stopwords')
nltk.download('punkt')

api = tweepy.API(auth)

if __name__ == '__main__':
    # stream = tweepy.Stream(auth=api.auth, listener=FileLogStreamListener())
    # stream.filter(track=['python'], languages=['en'])
    sentiment_calc = SentimentCalculator(['AFINN-emoticon-8.txt', 'AFINN-en-165.txt'])
    sentiment_calc.calculate('output.txt')

    frequency_calc = TermFrequencyCalculator()
    frequency_calc.calculate('output.txt')

    happy_or_calc = HappiestOriginCalculator()
    happy_or_calc.calculate('output.txt')
