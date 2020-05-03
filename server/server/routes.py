from .controller import get_detail, index, search
from aiohttp import web


def inject_routes(app: web.Application):
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/search', search)
    app.router.add_route('GET', '/detail', get_detail)
    app.router.add_route('GET', '/detail/{slug}', get_detail)
