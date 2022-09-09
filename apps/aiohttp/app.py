import typing

from aiohttp import web

if typing.TYPE_CHECKING:
    from aiohttp.web_routedef import AbstractRouteDef

    from config.settings import AppSettings


async def create_app(config: 'AppSettings', urls: typing.Iterable['AbstractRouteDef']) -> web.Application:
    app = web.Application()
    app.add_routes(urls)
    app_settings = {
        'config': config,
    }
    app.update(app_settings)
    return app
