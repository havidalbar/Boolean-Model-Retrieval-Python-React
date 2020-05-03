from .controller import index, search
from aiohttp import web


def inject_routes(app: web.Application):
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/search', search)
