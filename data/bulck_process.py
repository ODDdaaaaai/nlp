from data.store_data import pickle_data
from data.store_data import save_json
from data.store_data import unpickle_data
from text_proccessing.text_proccessing import clean

all_data = unpickle_data('resources/tagged_data/data_tagged.pckl')

for tweet in all_data:
    tweet.text = clean(tweet.text)

pickle_data(all_data, 'resources/tagged_data/data_tagged_cleaned.pckl')
save_json(all_data, 'resources/tagged_data/data_tagged_cleaned.json')
