import os
import sys
from retrieval.boolean_model import BooleanModel
from retrieval.file_utility import read_file
from retrieval.query_processing import infix_to_postfix, postfix_evaluator
from retrieval.sehatq_spider import start_spider


if __name__ == '__main__':
    data_filename: str = 'retrieval/resources/data_scrape.txt'

    for arg_index, arg in enumerate(sys.argv):
        if arg == '--data-filename':
            data_filename = sys.argv[arg_index + 1]
            break

    if not os.path.isfile(data_filename) or '--force-scrape' in sys.argv:
        start_spider(debug='--debug' in sys.argv, write_path=data_filename)

    data_content: str = read_file(data_filename)
    boolean_model: BooleanModel = BooleanModel(data_content)
    query = infix_to_postfix('trikiasis or trikomoniasis')
    print(postfix_evaluator(query, boolean_model))
