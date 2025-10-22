from flask import Flask
from compass_server.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from compass_server import routes