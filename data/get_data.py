import got

from data_source import DATA_BASE_DIRECTORY
from data_source import EVENTS
from data_source import PART_DATA_BASE_DIRECTORY
from model.Tweet import Tweet
from store_data import pickle_data
from store_data import save_json

# Search criteria
TOP_TWEETS = True
MAX_TWEETS = 5000
WITHIN = '1000mi'

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

                part_file_id = str(category_index) + str(event_index) + str(search_query_index) + str(near_index)

                # Save fetched tweets
                pickle_data(fetched_tweets, DATA_BASE_DIRECTORY + 'fetched_data.pckl')
                pickle_data(search_query_fetched_tweets,
                            PART_DATA_BASE_DIRECTORY + part_file_id + '/fetched_data.pckl')

                # Create list of custom model
                search_query_tweets = []

                for tweet in search_query_fetched_tweets:
                    search_query_tweets.append(Tweet(tweet.text, tweet.hashtags, [], []))

                tweets += search_query_tweets
                # Save custom tweets
                pickle_data(tweets, DATA_BASE_DIRECTORY + 'data.pckl')
                pickle_data(search_query_tweets,
                            PART_DATA_BASE_DIRECTORY + part_file_id + '/data.pckl')

                # Save tweets as JSON
                save_json(tweets, DATA_BASE_DIRECTORY + 'data.json')
                save_json(search_query_tweets,
                          PART_DATA_BASE_DIRECTORY + part_file_id + '/data.json')
