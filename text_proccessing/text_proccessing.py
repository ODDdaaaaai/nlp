# coding=utf-8
import codecs
import re

from nltk import word_tokenize
from nltk.corpus import stopwords


def clean(text):
    # Keep only arabic characters
    text = re.sub(u'[^\u0621-\u064A]', u' ', text)

    # Change ة to ه
    text = re.sub(u'\u0629', u'\u0647', text)

    # Change [ئ,ؤ,أ,إ,آ] to ء
    text = re.sub(u'[\u0622-\u0626]', u'\u0621', text)

    # Remove repeating letters such as هههههههههههههههه
    text = re.sub(r'(.)\1+', r'\1', text)

    # Remove extra spaces
    text = re.sub(u'(\s)+', u' ', text)

    return text


def remove_stop_words(tokens):
    stop_words = stopwords.words('arabic')
    with codecs.open('stop_words.txt', 'r', encoding='utf-8') as stop_words_file:
        for line in stop_words_file:
            stop_words.append(line.split('\r')[0])
    return [token for token in tokens if token not in stop_words]


def tokenize(text):
    return word_tokenize(text)


def remove_duplicates(sentences):
    lines_set = set()
    for sentence in sentences:
        if sentence not in lines_set:
            lines_set.add(sentence)
    return list(lines_set)
