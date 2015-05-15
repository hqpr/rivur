import os

from settings import BASE_DIR
from settings import STATIC_URL

DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
MEDIA_ROOT = '../media/'