import os
class Config:
    SECRET_KEY = os.urandom(32).hex()
    MAX_CONTENT_LENGTH = 1024*1024