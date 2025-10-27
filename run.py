import os
from compass_server import app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    app2 = DispatcherMiddleware(None, {os.getenv("SUBPATH"): app})
    run_simple(os.getenv("HOST"), int(os.getenv("PORT")), app2, use_reloader=os.getenv("DEBUG")=="true", use_debugger=os.getenv("DEBUG")=="true")
