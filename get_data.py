import codecs
import json
import os
import pickle

import got

from data_source.data_source import DATA_BASE_DIRECTORY
from data_source.data_source import EVENTS
from data_source.data_source import PART_DATA_BASE_DIRECTORY
from model.Tweet import Tweet

# Search criteria
TOP_TWEETS = True
MAX_TWEETS = 5000
WITHIN = '1000mi'


def pickle_data(data, file_path):
    part_file_directory = os.path.dirname(file_path)
    if not os.path.exists(part_file_directory):
        os.makedirs(part_file_directory)
    pickle.dump(data, open(file_path, 'wb'))


def save_json(data, file_path):
    part_file_directory = os.path.dirname(file_path)
    if not os.path.exists(part_file_directory):
        os.makedirs(part_file_directory)
    with codecs.open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump([element.__dict__ for element in data], outfile, indent=4, ensure_ascii=False)

    outfile.close()


# List of fetched tweets
fetched_tweets = []

tweets = []

# Get tweets
for category_index, category in enumerate(EVENTS):
    for event_index, event in enumerate(category):
        for search_query_index, search_query in enumerate(event.search_queries):
            for near_index, near in enumerate(event.near):
                print('Fetching: category: ' + str(category_index) + ' Event: ' + str(
                    event_index) + ' Search query: ' + search_query + ' Near: ' + near)

                search_query_fetched_tweets = []

                tweetCriteria = got.manager.TweetCriteria().setTopTweets(TOP_TWEETS).setSince(event.since).setUntil(
                    event.until).setNear(near).setWithin(WITHIN).setQuerySearch(search_query).setMaxTweets(MAX_TWEETS)
                search_query_fetched_tweets += got.manager.TweetManager.getTweets(tweetCriteria)

                fetched_tweets += search_query_fetched_tweets

                print('Fetched ' + str(len(search_query_fetched_tweets)) + ' new tweets successfully')
                print('Fetched ' + str(len(fetched_tweets)) + ' total tweets\n')

                # Save fetched tweets
                pickle_data(fetched_tweets, DATA_BASE_DIRECTORY + 'fetched_data.pckl')
                pickle_data(search_query_fetched_tweets,
                            PART_DATA_BASE_DIRECTORY + str(search_query_index) + str(near_index) + '/fetched_data.pckl')

                # Create list of custom model
                search_query_tweets = []

                for tweet in search_query_fetched_tweets:
                    search_query_tweets.append(Tweet(tweet.text, tweet.hashtags, [], []))

                tweets += search_query_tweets
                # Save custom tweets
                pickle_data(tweets, DATA_BASE_DIRECTORY + 'data.pckl')
                pickle_data(search_query_tweets,
                            PART_DATA_BASE_DIRECTORY + str(search_query_index) + str(near_index) + '/data.pckl')

                # Save tweets as JSON
                save_json(tweets, DATA_BASE_DIRECTORY + 'data.json')
                save_json(search_query_tweets,
                          PART_DATA_BASE_DIRECTORY + str(search_query_index) + str(near_index) + '/data.json')
