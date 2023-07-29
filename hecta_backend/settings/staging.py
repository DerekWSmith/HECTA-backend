from .development import *

DEBUG = False
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
