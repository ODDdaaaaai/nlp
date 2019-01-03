# coding=utf-8
import got

from model.Event import Event

# Search criteria
TOP_TWEETS = True
MAX_TWEETS = 40
WITHIN = '1000mi'

# Locations
NEAR = ['السعودية', 'مصر']

# Events to search for
HAPPY_EVENTS = [
    Event(['فطر', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2016-7-5', '2016-7-8'),
    Event(['الفطر', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2017-6-24', '2017-6-27'),
    Event(['فطر', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2018-6-14', '2018-6-16'),

    Event(['الأضحى', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2016-9-11', '2016-9-15'),
    Event(['الأضحى', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2017-8-31', '2018-9-4'),
    Event(['الأضحى', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2018-8-20', '2018-8-24'),

    Event(['المولد', 'كل عام وانتم بخير'], '2016-12-10', '2016-12-10'),
    Event(['المولد', 'كل عام وانتم بخير'], '2017-11-30', '2017-12-1'),
    Event(['المولد', 'كل عام وانتم بخير'], '2018-11-19', '2018-11-21'),

    Event(['السنة الهجرية', 'كل عام وانتم بخير'], '2016-10-1', '2016-10-1'),
    Event(['السنة الهجرية', 'كل عام وانتم بخير'], '2017-9-20', '2017-9-21'),
    Event(['السنة الهجرية', 'كل عام وانتم بخير'], '2018-9-10', '2018-9-11'),

    Event(['المسيح', 'كريسمس', 'عيد مجيد', 'ميلاد', "سعيد"], '2016-12-24', '2016-12-25'),
    Event(['المسيح', 'كريسمس', 'عيد مجيد', 'ميلاد', "سعيد"], '2017-12-24', '2017-12-25'),
    Event(['المسيح', 'كريسمس', 'عيد مجيد', 'ميلاد', "سعيد"], '2018-12-24', '2018-12-25'),

    Event(['رأس السنة', 'كل عام و أنتم بخير'], '2016-12-31', '2017-1-1'),
    Event(['رأس السنة', 'كل عام و أنتم بخير'], '2017-12-31', '2018-1-1'),
    Event(['رأس السنة', 'كل عام و أنتم بخير'], '2018-12-31', '2019-1-1'),

    Event(['الأم'], '2016-03-21', '2016-03-22'),
    Event(['الأم'], '2017-03-21', '2017-03-22'),
    Event(['الأم'], '2018-03-21', '2018-03-22'),
]

ANGRY_EVENTS = [

]

EVENTS = [
    HAPPY_EVENTS
]

# List of tweets
tweets = []

# Get tweets
for near in NEAR:
    for category in EVENTS:
        for event in category:
            for search_query in event.search_queries:
                tweetCriteria = got.manager.TweetCriteria().setTopTweets(TOP_TWEETS).setSince(event.since).setUntil(
                    event.until).setNear(near).setWithin(WITHIN).setQuerySearch(search_query).setMaxTweets(MAX_TWEETS)
                tweets += got.manager.TweetManager.getTweets(tweetCriteria)

# Print fetched tweets
count = 1
for tweet in tweets:
    print(str(count) + tweet.text.encode('utf-8'))
    count += 1

# tweets_text = []
# tweets_hashtags = []
#
# for searchQuery in QUERIES:
#     tweetCriteria = got.manager.TweetCriteria().setTopTweets(TOP_TWEETS).setQuerySearch(searchQuery).setSince(SINCE).setUntil(
#         UNTIL).setNear(NEAR).setMaxTweets(MAX_TWEETS)
#     tweets += got.manager.TweetManager.getTweets(tweetCriteria)
#
# file_tweets_text = open('data\\tweets_text.txt', 'wb')
# file_tweets_hashtags = open('data\\tweets_hashtags.txt', 'wb')
# file_tweets_stats = open('data\\tweets_stats.txt', 'wb')
#
# for tweet in tweets:
#     tweet_text = tweet.text.encode('utf-8')
#     file_tweets_text.write(tweet_text)
#     file_tweets_text.write("\n")
#     tweets_text.append(tweet_text)
#     tweet_hashtags = tweet.hashtags.encode('utf-8')
#     file_tweets_hashtags.write(tweet_hashtags)
#     file_tweets_hashtags.write("\n")
#     tweets_hashtags.append(tweet_hashtags)
#
# file_tweets_stats.write("Total tweets = " + str(len(tweets)))
# file_tweets_stats.write("Total hashtags = " + str(len(tweets_hashtags)))
#
# file_tweets_text.close()
# file_tweets_hashtags.close()
# file_tweets_stats.close()
