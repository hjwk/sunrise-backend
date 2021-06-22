import os

from flask import Flask
from flask_cors import CORS


def create_app(test_config=None):
    # instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'sunrise.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from backend.alarms import alarms_bp
    app.register_blueprint(alarms_bp, url_prefix='/alarms')

    return app