import os

env = os.environ.get("ENVIRONMENT")

if env in ["development", "dev"]:
    from .development import *
elif env in ["staging", "stage"]:
    from .staging import *
elif env in ["production", "prod"]:
    from .production import *
