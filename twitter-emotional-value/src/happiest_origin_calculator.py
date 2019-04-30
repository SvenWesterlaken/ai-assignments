import src, json, geonamescache, re, operator
from geonamescache.mappers import country as country_mapper

class HappiestOriginCalculator(object):

    def __init__(self):
        self.gc = geonamescache.GeonamesCache()
        self.geo_countries = self.gc.get_countries().values()
        self.geo_cities = self.gc.get_cities().values()
        self.isoToNameMapper = country_mapper(from_key='iso', to_key='name')

    def mapLocationString(self, str):
        str = str.strip()

        # if the string is a country make sure it matches by converting to uppercase
        return str.upper() if len(str) == 2 else str

    def formatSentiment(self, sentiment):
        sm = str(round(float(sentiment), 2))

        return '0.0' if sm == '-0.0' else sm

    def calculate(self, tweetFileName, sentimentFileName = 'sentiment_scores.txt', outputFileName = 'happiest_origins.txt'):
        rf, of = src.getFiles(tweetFileName, outputFileName)
        sf = src.getFile(sentimentFileName)

        sentiments = sf.readlines()

        countries = {}
        o_str = ''

        for i, line in enumerate(rf):
            sentiment = int(sentiments[i])
            tweet = json.loads(line)
            origin = None

            # get country if place object available
            if tweet['place']:
                origin = tweet['place']['country']
            # else get location of the user if available
            elif tweet['user']['location']:
                # split to increase posibility to match either a country or a city (most items will contain multiple parts that could match)
                loc_l = list(map(self.mapLocationString, tweet['user']['location'].split(',')))

                # placeholder
                match = None

                for l in loc_l:
                    # if no match already found
                    if not match:
                        # search in the list of countries and cities for any possible match
                        match = next((country['name'] for country in self.geo_countries if l in country.values()), None) or next((city['countrycode'] for city in self.geo_cities if l in city.values()), None)

                # if match was a city, convert to country with the available country code
                if match and len(match) == 2:
                    match = self.isoToNameMapper(match)

                origin = match

            # if origin available calculate sentiment and add te result to the countries dictionary
            if origin:
                if origin in countries:

                    countries[origin] = (countries[origin] + sentiment) / 2
                else:
                    countries[origin] = sentiment

        countries = sorted(countries.items(), key=operator.itemgetter(1), reverse=True)

        for c, sm in countries:
            o_str += c + "\t " + self.formatSentiment(sm) + "\n"

        of.write(o_str)

        print('--------------------------------------------------------------')
        print('The happiest country is:', countries[0][0])
        print('--------------------------------------------------------------')

        rf.close()
        sf.close()
        of.close()

        return countries[0]
