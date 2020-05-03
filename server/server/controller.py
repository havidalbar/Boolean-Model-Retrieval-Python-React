from aiohttp import web
from .utility import load_model_pickle
from retrieval.boolean_model import BooleanModel
from retrieval.data_model import DataModel
from retrieval.query_processing import infix_to_postfix, postfix_evaluator
from typing import Dict, List, Set


def index(request: web.Request):
    return web.json_response({"message": "Welcome to Boolean Retrieval Model API!"})


def search(request: web.Request):
    boolean_model: BooleanModel = load_model_pickle()
    try:
        query: str = request.query.get('q', '').strip()
        postfix_query: List[int] = infix_to_postfix(query)
        evaluator_result: Set[int] = postfix_evaluator(postfix_query, boolean_model)

        result_docs: List[Dict[str, str]] = [doc.asdict(output_keys=['slug', 'title', 'img', 'cleaned'])
                                             for doc in boolean_model.get_documents(evaluator_result)]

        return web.json_response({"message": "Success!", "data": result_docs})
    except:
        return web.json_response({"message": "Invalid Query!"}, status=422)


def get_detail(request: web.Request):
    boolean_model: BooleanModel = load_model_pickle()
    result: DataModel = boolean_model.get_document_by_slug(
        request.match_info.get('slug', ''))

    if result is None:
        return web.json_response({"message": "Disease Not Found!"}, status=404)

    return web.json_response({
        "message": "Success!",
        "data": result.asdict(output_keys=['url', 'title', 'img', 'content'])
    })
