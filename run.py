import os
from compass_server import app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from waitress import serve
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    app2 = DispatcherMiddleware(None, {os.getenv("SUBPATH"): app})
    if os.getenv("DEBUG") == "true":
        from werkzeug.serving import run_simple
        run_simple(os.getenv("HOST"), int(os.getenv("PORT")), app2, use_reloader=True, use_debugger=True)
    else:
        serve(app2, host=os.getenv("HOST"), port=os.getenv("PORT"))
