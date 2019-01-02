# coding=utf-8
import got

from model.Event import Event

TOP_TWEETS = True
EVENTS = [
    Event(['فطر', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2018-6-14', '2018-6-16'),
    Event(['الأضحى', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2018-8-20', '2018-8-24'),
    Event(['المسيح', 'كريسمس', 'عيد مجيد', 'ميلاد', "سعيد"], '2018-12-24', '2018-12-25'),
    Event(['رأس السنة', 'كل عام و أنتم بخير'], '2018-12-31', '2019-1-1'),
    Event(['الفطر', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2018-6-24', '2018-6-27'),
    Event(['الأضحى', 'عيد', 'سعيد', 'كل عام و أنتم بخير'], '2018-8-31', '2018-9-4'),
    Event(['المسيح', 'كريسمس', 'عيد مجيد', 'ميلاد', "سعيد"], '2017-12-24', '2017-12-25'),
    Event(['رأس السنة', 'كل عام و أنتم بخير'], '2017-12-31', '2018-1-1')
]
NEAR = ['السعودية', 'مصر']
MAX_TWEETS = 40
WITHIN = '1000mi'

tweets = []

for near in NEAR:
    for event in EVENTS:
        for search_query in event.search_queries:
            tweetCriteria = got.manager.TweetCriteria().setTopTweets(TOP_TWEETS).setSince(event.since).setUntil(
                event.until).setNear(near).setWithin(WITHIN).setQuerySearch(search_query).setMaxTweets(MAX_TWEETS)
            tweets += got.manager.TweetManager.getTweets(tweetCriteria)

count = 1
for tweet in tweets:
    print(str(count) + tweet.text.encode('utf-8'))
    count += 1
