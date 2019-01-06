import codecs
import json
import os
import pickle


def pickle_data(data, file_path):
    part_file_directory = os.path.dirname(file_path)
    if not os.path.exists(part_file_directory):
        os.makedirs(part_file_directory)
    with open(file_path, 'wb') as out:
        pickle.dump(data, out)

    out.close()


def unpickle_data(file_path):
    return pickle.load(open(file_path, 'rb'))


def save_json(data, file_path):
    part_file_directory = os.path.dirname(file_path)
    if not os.path.exists(part_file_directory):
        os.makedirs(part_file_directory)
    with codecs.open(file_path, 'w', encoding='utf-8') as out:
        json.dump([element.__dict__ for element in data], out, indent=4, ensure_ascii=False)

    out.close()


def read_json(file_path):
    return json.load(codecs.open(file_path, 'r', encoding='utf-8'))
