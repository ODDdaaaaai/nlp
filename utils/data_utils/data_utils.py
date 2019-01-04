import codecs
import json
import os
import pickle


def to_file_pickle(data, file_path):
    part_file_directory = os.path.dirname(file_path)
    if not os.path.exists(part_file_directory):
        os.makedirs(part_file_directory)
    with open(file_path, 'wb') as out:
        pickle.dump(data, out)
        out.close()


def to_file_json(data, file_path):
    part_file_directory = os.path.dirname(file_path)
    if not os.path.exists(part_file_directory):
        os.makedirs(part_file_directory)
    with codecs.open(file_path, 'w', encoding='utf-8') as out:
        json.dump([datum.__dict__ for datum in data], out, indent=4, ensure_ascii=False)
        out.close()
