import os
import pickle
from retrieval.boolean_model import BooleanModel
from retrieval.file_utility import read_file


def load_model_pickle() -> BooleanModel:
    data_filename: str = 'retrieval/resources/data_scrape.txt'
    pickle_filename: str = 'boolean_model.pickle'

    boolean_model: BooleanModel = None
    if not os.path.isfile(pickle_filename):
        data_content: str = read_file(data_filename)
        boolean_model = BooleanModel(data_content)
    else:
        boolean_model_file = open(pickle_filename, 'rb')
        boolean_model = pickle.load(boolean_model_file)
        boolean_model_file.close()

    return boolean_model
