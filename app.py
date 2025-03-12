from flask import Flask
from py_term_helpers import *
from ipdb import set_trace


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config:
        app.config.from_mapping(test_config)

    
    from server.routes import flask_app
    app.register_blueprint(flask_app)

    return app


if __name__ == '__main__':
    PORT = 5555
    top_wrap(f"FLASK APP RUNNING ON PORT={PORT}")
    app = create_app()
    app.run(port=PORT, debug=False)
