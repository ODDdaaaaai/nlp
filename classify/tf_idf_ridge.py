import random

import nltk

from classify.classify import accuracy
from classify.classify import ridge_classifier
from data.store_data import pickle_data
from data.store_data import unpickle_data
from feature.feature import tf_idf
from text_proccessing.text_proccessing import tokenize

tweets = unpickle_data('resources/tagged_data/data_tagged_cleaned.pckl')

random.shuffle(tweets)

X_train = [tweet.text for tweet in tweets[:16000]]
y_train = [tweet.feelings[0] for tweet in tweets[:16000]]
X_test = [tweet.text for tweet in tweets[-4000:]]
y_test = [tweet.feelings[0] for tweet in tweets[-4000:]]

all_words = []
for sample in X_train:
    words = tokenize(sample)
    for w in words:
        all_words.append(w)

all_words_freq = nltk.FreqDist(all_words)

training_features, testing_features, vocabulary = tf_idf(X_train, X_test)

classifier = ridge_classifier(training_features, y_train)

pickle_data(classifier, 'resources/classifiers/tf_idf_ridge.cls')

test_predicted_labels = classifier.predict(testing_features)
test_predicted_scores = classifier.decision_function(testing_features)

for i in range(3):
    print('Review:\t{}\nPredicted label:\t{}\n\n'.format(
        X_test[i][:100].encode('utf-8') + "...", test_predicted_labels[i].encode('utf-8'))
    )

print('Tfidf Accuracy: ' + str(accuracy(y_test, test_predicted_labels) * 100) + '%')
