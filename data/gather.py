from data.store_data import *
from model.Tweet import Tweet

fetched_data = pickle.load(open('resources/fetched_data/v1/fetched_data.pckl', 'rb'))
fetched_data += pickle.load(open('resources/fetched_data/v2/fetched_data.pckl', 'rb'))
fetched_data += pickle.load(open('resources/fetched_data/v3/fetched_data.pckl', 'rb'))
fetched_data += pickle.load(open('resources/fetched_data/v4/fetched_data.pckl', 'rb'))

pickle_data(fetched_data, 'resources/fetched_data/final/fetched_data.pckl')

tweets = []

for tweet in fetched_data:
    tweets.append(Tweet(tweet.text, tweet.hashtags, [], []))

pickle_data(tweets, 'resources/fetched_data/final/data.pckl')
save_json(tweets, 'resources/fetched_data/final/data.json')
