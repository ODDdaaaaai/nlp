import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer


def bag_of_words(tokens, vocabulary, dictionary_size):
    result_vector = np.zeros(dictionary_size)
    for token in tokens:
        if token in vocabulary:
            result_vector[vocabulary[token]] += 1

    return result_vector


def tf_idf(training_samples, testing_samples):
    vectorizer = TfidfVectorizer(min_df=3, max_df=0.9, ngram_range=(1, 2))
    vectorizer.fit(training_samples)
    training_features = vectorizer.transform(training_samples)
    testing_features = vectorizer.transform(testing_samples)

    return training_features, testing_features, vectorizer.vocabulary_


def extract_features(sample, features):
    features = {}
    for feature in features:
        features['contains(%s)' % feature] = (feature in sample)
    return features
