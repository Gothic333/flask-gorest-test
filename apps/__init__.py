from flask import Flask
from config import config as Config


def create_app(config_type):
    app = Flask(__name__)

    app.config.from_object(Config[config_type])
    Config[config_type].init_app(app)

    from .blueprints.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .blueprints.users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix="/users")

    from .blueprints.errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    return app
