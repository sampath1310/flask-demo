import logging
import os
from flask import Flask,make_response,jsonify

import config
from api.isbn_blueprint import isbn

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
    logger.info('Starting app in' + config.APP_ENV + ' environment')
    app = Flask(__name__)
    app.register_blueprint(isbn)
    app.config.from_object('config')

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/pot/<id>')
    def hello(id):
        return id

    return app

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({'error': 'bad_request'}), 400)


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
