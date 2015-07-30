import gevent.monkey
gevent.monkey.patch_all()

from flask import Flask
from app import log

def create_app():
    app = Flask(__name__)
    from app.api import api
    app.register_blueprint(api)
    log.setup_logging()
    return app