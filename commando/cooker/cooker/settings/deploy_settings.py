from .base_settings import *  # NOQA
from .base_settings import get_environ

DEBUG = False
# Set this to your prod host
ALLOWED_HOSTS = []

# You can choose a default STATIC_URL for prod such ass
# "//username.github.io/namespace..."
STATIC_URL = get_environ('STATIC_URL')
