from .routes import inject_routes
from aiohttp import web


app = web.Application()
inject_routes(app)
