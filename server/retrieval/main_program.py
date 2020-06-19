import os
import pickle
import sys
from .boolean_model import BooleanModel
from .data_model import DataModel
from .file_utility import read_file
from .query_processing import infix_to_postfix, postfix_evaluator
from .sehatq_spider import start_spider
from typing import List, Set


if __name__ == '__main__':
    data_filename: str = 'retrieval/resources/data_scrape.txt'
    pickle_filename: str = 'boolean_model.pickle'

    for arg_index, arg in enumerate(sys.argv):
        if arg == '--data-filename':
            data_filename = sys.argv[arg_index + 1]
            break

    rescrape: bool = not os.path.isfile(
        data_filename) or '--force-scrape' in sys.argv

    if rescrape:
        start_spider(debug='--debug' in sys.argv, write_path=data_filename)

    boolean_model: BooleanModel = None
    if rescrape or not os.path.isfile(pickle_filename) or '--force-indexing' in sys.argv:
        data_content: str = read_file(data_filename)
        boolean_model = BooleanModel(data_content)
    else:
        boolean_model_file = open(pickle_filename, 'rb')
        boolean_model = pickle.load(boolean_model_file)
        boolean_model_file.close()

    query: List[int] = infix_to_postfix('gatal and (merah or perih)')
    evaluator_result: Set[int] = postfix_evaluator(query, boolean_model)
    print(evaluator_result)
    result_docs: List[DataModel] = boolean_model.get_documents(
        evaluator_result)
    for doc in result_docs:
        print(doc.get_title())
