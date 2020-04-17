from aiohttp import web


def index(request):
    return web.Response(text="Hello World")

app = web.Application()
app.router.add_route('GET', '/', index)