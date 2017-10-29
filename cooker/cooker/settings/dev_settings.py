import typing
from .base_settings import *  # NOQA

DEBUG = True

INTERNAL_IPS = ['127.0.0.1', 'localhost', '10.0.2.2']
STATIC_ASSET_URL = '//localhost:3000/'

INSTALLED_APPS: typing.List = INSTALLED_APPS + ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # NOQA

ALLOWED_HOSTS = ['*']
