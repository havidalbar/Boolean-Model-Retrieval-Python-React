import json
import time
from aiohttp import web
from .utility import load_model_pickle
from retrieval.boolean_model import BooleanModel
from retrieval.data_model import DataModel
from retrieval.query_processing import infix_to_postfix, postfix_evaluator
from typing import Dict, List, Set


def json_inject_execution_time(func):
    def inner_wrapper(*args, **kwargs):
        start_time = time.time()
        result: web.Response = func(*args, **kwargs)
        execution_time = time.time() - start_time
        payload: Dict = json.loads(result.text)
        payload['execution_time'] = execution_time
        result.text = json.dumps(payload)

        return result

    return inner_wrapper


@json_inject_execution_time
def index(request: web.Request):
    return web.json_response({"message": "Welcome to Boolean Retrieval Model API!"})


@json_inject_execution_time
def search(request: web.Request):
    boolean_model: BooleanModel = load_model_pickle()
    try:
        query: str = request.query.get('q', '').strip()
        current_page: int = int(request.query.get('page', 1))
        page_size_limit: int = int(request.query.get('limit', 10))

        postfix_query: List[int] = infix_to_postfix(query)
        evaluator_result: Set[int] = postfix_evaluator(postfix_query, boolean_model)

        result_docs: List[Dict[str, str]] = [doc.asdict(output_keys=['slug', 'title', 'img', 'summary'])
                                             for doc in boolean_model.get_documents(evaluator_result)]

        total_result: int = len(result_docs)
        offset: int = (current_page - 1) * page_size_limit
        result_docs = result_docs[offset:current_page * page_size_limit]

        return web.json_response({
            "message": "Success!",
            "meta": {
                "page": current_page,
                "size": len(result_docs),
                "limit": page_size_limit,
                "total": total_result
            },
            "data": result_docs
        })
    except:
        return web.json_response({"message": "Invalid Query!"}, status=422)


@json_inject_execution_time
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
