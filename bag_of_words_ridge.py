import random

import nltk
from scipy import sparse as sp_sparse

from classify.classify import accuracy
from classify.classify import ridge_classifier
from data.store_data import pickle_data
from data.store_data import unpickle_data
from feature.feature import bag_of_words
from text_proccessing.text_proccessing import remove_stop_words
from text_proccessing.text_proccessing import tokenize

tweets = unpickle_data('resources/tagged_data/data_tagged_cleaned.pckl')

random.shuffle(tweets)

X_train = [tweet.text for tweet in tweets[:16000]]
y_train = [tweet.feelings[0] for tweet in tweets[:16000]]
X_test = [tweet.text for tweet in tweets[-4000:]]
y_test = [tweet.feelings[0] for tweet in tweets[-4000:]]

all_words = []
for sample in X_train:
    words = remove_stop_words(tokenize(sample))
    for word in words:
        all_words.append(word)

all_words_freq = nltk.FreqDist(all_words)

DICT_SIZE = 500
INDEX_TO_WORDS = {i: word[0] for i, word in enumerate(all_words_freq.most_common(DICT_SIZE))}
WORDS_TO_INDEX = {word: i for i, word in INDEX_TO_WORDS.items()}
ALL_WORDS = WORDS_TO_INDEX.keys()

training_features = sp_sparse.vstack(
    [sp_sparse.csr_matrix(bag_of_words(remove_stop_words(tokenize(text)), WORDS_TO_INDEX, DICT_SIZE)) for text in
     X_train])
testing_features = sp_sparse.vstack(
    [sp_sparse.csr_matrix(bag_of_words(remove_stop_words(tokenize(text)), WORDS_TO_INDEX, DICT_SIZE)) for text in
     X_test])

classifier = ridge_classifier(training_features, y_train)

pickle_data(classifier, 'resources/classifiers/bag_ridge.cls')

test_predicted_labels = classifier.predict(testing_features)
test_predicted_scores = classifier.decision_function(testing_features)

for i in range(3):
    print('Review:\t{}\nPredicted label:\t{}\n\n'.format(
        X_test[i][:100].encode('utf-8') + "...", test_predicted_labels[i].encode('utf-8'))
    )

print('Bag-of-words Accuracy: ' + str(accuracy(y_test, test_predicted_labels) * 100) + '%')
