import os

def get_backend_url():
    return os.getenv("BACKEND_URL", None)