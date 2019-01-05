# coding=utf-8
import re

from nltk import word_tokenize


def clean(text):
    # Kepp only arabic characters
    text = re.sub(u'[^\u0621-\u064A]', u' ', text)

    # Change ة to ه
    text = re.sub(u'\u0629', u'\u0647', text)

    # Change [ئ,ؤ,أ,إ,آ] to ء
    text = re.sub(u'[\u0622-\u0626]', u'\u0621', text)

    # Remove repeating letters such as هههههههههههههههه
    text = re.sub(r'(.)\1+', r'\1', text)

    # Remove extra spaces
    text = re.sub(u'(\s)+', ' ', text)

    return text


def tokenize(text):
    return word_tokenize(text, 'arabic')


print(tokenize(clean(u'ان أحب أكل البطاط المقلية')))
