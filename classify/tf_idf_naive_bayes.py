import random

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from data.store_data import unpickle_data

tweets = unpickle_data('resources/tagged_data/data_tagged_cleaned.pckl')

random.shuffle(tweets)

X_train = [tweet.text for tweet in tweets[:16000]]
y_train = [tweet.feelings[0] for tweet in tweets[:16000]]
X_test = [tweet.text for tweet in tweets[-4000:]]
y_test = [tweet.feelings[0] for tweet in tweets[-4000:]]

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, y_train)

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
                     ])

text_clf = text_clf.fit(X_train, y_train)

predicted = text_clf.predict(X_test)

precision = precision_score(y_test, predicted, average='macro')
recall = recall_score(y_test, y_test, average='macro')

for i in range(3):
    print('Review:\t{}\nPredicted label:\t{}\n\n'.format(
        X_test[i][:100].encode('utf-8') + "...", predicted[i][:100])
    )

print('TF-IDF Naive Bayes accuracy = ' + str(np.mean(predicted == y_test) * 100) + '%')

print('Precision score: {0:0.2f}'.format(precision))
print('Recall score: {0:0.2f}'.format(recall))
