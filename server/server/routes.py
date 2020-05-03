import aiohttp_cors
import os
from .controller import get_detail, index, search
from aiohttp import web


def inject_routes(app: web.Application):
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/search', search)
    app.router.add_route('GET', '/detail', get_detail)
    app.router.add_route('GET', '/detail/{slug}', get_detail)

    if int(os.getenv('IS_DEV', 1)) != 0:
        cors = aiohttp_cors.setup(app, defaults={
            "*": aiohttp_cors.ResourceOptions()
        })

        for route in app.router.routes():
            cors.add(route)
