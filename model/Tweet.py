class Tweet:
    count = 0

    def __init__(self, text, hashtags, feelings, topics):
        self.text = text
        self.hashtags = hashtags
        self.feelings = feelings
        self.topics = topics
