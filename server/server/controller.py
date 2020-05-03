import os
import pickle
from aiohttp import web
from retrieval.boolean_model import BooleanModel
from retrieval.data_model import DataModel
from retrieval.file_utility import read_file
from retrieval.query_processing import infix_to_postfix, postfix_evaluator
from typing import Dict, List, Set


def index(request: web.Request):
    return web.json_response({"message": "Welcome to Boolean Retrieval Model API!"})


def search(request: web.Request):
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

    try:
        query: str = request.query.get('q', '').strip()
        postfix_query: List[int] = infix_to_postfix(query)
        evaluator_result: Set[int] = postfix_evaluator(postfix_query, boolean_model)

        result_docs: List[Dict[str, str]] = [doc.asdict(output_keys=['slug', 'title', 'img', 'cleaned'])
                                             for doc in boolean_model.get_documents(evaluator_result)]

        return web.json_response({"message": "Success!", "data": result_docs})
    except:
        return web.json_response({"message": "Invalid Query!"}, status=422)
