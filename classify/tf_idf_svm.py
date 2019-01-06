import random

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

from data.store_data import unpickle_data

tweets = unpickle_data('resources/tagged_data/data_tagged_cleaned.pckl')

random.shuffle(tweets)

X_train = [tweet.text for tweet in tweets[:16000]]
y_train = [tweet.feelings[0] for tweet in tweets[:16000]]
X_test = [tweet.text for tweet in tweets[-4000:]]
y_test = [tweet.feelings[0] for tweet in tweets[-4000:]]

text_clf_svm = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf-svm',
                          SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42)), ])

_ = text_clf_svm.fit(X_train, y_train)
predicted_svm = text_clf_svm.predict(X_test)
np.mean(predicted_svm == X_test)

for i in range(3):
    print('Review:\t{}\nPredicted label:\t{}\n\n'.format(
        X_test[i][:100].encode('utf-8') + "...", predicted_svm[i][:100])
    )

print('TF-IDF SVM accuracy ' + str(np.mean(predicted_svm == y_test) * 100) + '%')
