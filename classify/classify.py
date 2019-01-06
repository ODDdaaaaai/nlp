from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import accuracy_score


def ridge_classifier(samples, labels):
    classifier = RidgeClassifier()
    classifier.fit(samples, labels)
    return classifier


def accuracy(test_labels, predicted_labels):
    return accuracy_score(test_labels, predicted_labels)
