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


def save_json(data, file_path):
    part_file_directory = os.path.dirname(file_path)
    if not os.path.exists(part_file_directory):
        os.makedirs(part_file_directory)
    with codecs.open(file_path, 'w', encoding='utf-8') as outfile:
        json.dump([element.__dict__ for element in data], outfile, indent=4, ensure_ascii=False)

    outfile.close()
