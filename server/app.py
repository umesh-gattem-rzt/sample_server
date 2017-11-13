import argparse
import logging
import os
import sys

from flask import Flask, Blueprint

path = "/".join(os.getcwd().split('/')[:-1])
sys.path.append(path)
from server import SAMPLE_CONFIG
from server.api.restplus import api

app = Flask(__name__)

logger = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['FLASK_HOST'] = SAMPLE_CONFIG.ServerConfig.FLASK_HOST
    flask_app.config['FLASK_PORT'] = SAMPLE_CONFIG.ServerConfig.FLASK_PORT
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = SAMPLE_CONFIG.ServerConfig.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = SAMPLE_CONFIG.ServerConfig.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = SAMPLE_CONFIG.ServerConfig.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = SAMPLE_CONFIG.ServerConfig.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)
    print()


def main():
    initialize_app(app)
    parser = argparse.ArgumentParser(description='PyFlow: Debugger')
    parser.add_argument('-port', help="Run Flask", required=True)
    args = vars(parser.parse_args())
    if args['port']:
        app.run(host=app.config['FLASK_HOST'], port=args['port'])
    app.run(debug=SAMPLE_CONFIG.ServerConfig.FLASK_DEBUG)


if __name__ == "__main__":
    from server.api.sample_extension import *
    main()
