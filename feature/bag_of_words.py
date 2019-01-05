import numpy as np

from text_proccessing.text_proccessing import *


def bag_of_words(sentence, vocabulary):
    sentence_words = remove_stop_words(tokenize(clean(sentence)))
    bag = np.zeros(len(vocabulary))
    for sentence_word in sentence_words:
        for i, vocabulary_word in enumerate(vocabulary):
            if vocabulary_word == sentence_word:
                bag[i] += 1

    return np.array(bag)
