# coding='utf-8'
import random

import nltk

from data.store_data import pickle_data
from data.store_data import unpickle_data
from feature.feature import extract_features
from text_proccessing.text_proccessing import remove_stop_words
from text_proccessing.text_proccessing import tokenize

tweets = unpickle_data('resources/tagged_data/data_tagged_cleaned.pckl')

documents = [([], str)]
for tweet in tweets:
    try:
        documents.append((remove_stop_words(tokenize(tweet.text)), tweet.feelings[0]))
    except IndexError:
        pass

random.shuffle(documents)

all_words = []
for sample in documents[:10000]:
    words = sample[0]
    for word in words:
        all_words.append(word)

freq = nltk.FreqDist(all_words)
most_common_words = freq.most_common()[500:1000]

final_features = []
for word in most_common_words:
    final_features.append(word[0])

feature_set = [(extract_features(sentence, final_features), tag) for (sentence, tag) in documents[:16000]]
train_set, test_set = feature_set[:16000], feature_set[-4000:]
classifier = nltk.NaiveBayesClassifier.train(train_set)

pickle_data(classifier, 'resources/classifiers/naive_bayes.cls')

test_data = tweets[-4000:]

for i in range(3):
    print('Review:\t{}\nPredicted label:\t{}\n\n'.format(
        test_data[i].text.encode('utf-8') + "...",
        classifier.classify(extract_features(test_data[i].text, final_features)))
    )

print('Naive bayes Accuracy: ' + str(nltk.classify.accuracy(classifier, test_set) * 100) + '%')
