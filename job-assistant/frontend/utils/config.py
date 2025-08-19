import os

def get_backend_url():
    return os.getenv("BACKEND_URL", "http://127.0.0.1:8000")