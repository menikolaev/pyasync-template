from aiohttp import web

from apps.aiohttp.app import create_app
from apps.aiohttp.urls import urls
from config.settings import AppSettings

if __name__ == '__main__':
    config = AppSettings()
    web.run_app(create_app(config, urls), port=config.port)
