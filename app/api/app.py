"""The app module, containing the app factory function."""

from flask import Flask #(Flask, redirect, url_for)

from app.api.settings import (ProdConfig, Config)

def create_app(config_object: Config = ProdConfig)->Flask:
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    Keyword Arguments:
        config_object {Config} -- A configuration object to be used (default: {ProdConfig})

    Returns:
        Flask -- Returns a Flask object
    """

    app = Flask(__name__.split('.')[0])

    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    register_commands(app)

    @app.route('/', methods=['GET'])
    def root_main()->str:
        return '<div id=\'info\' style=\'text-align:center\'><h1>Hello World!</h1><br><h2>This is the API for B2W Star Wars Challenge!</h2><br><br><br><h3>RAPHAEL SATHLER - 2019.</h3></div>'

    return app


def register_extensions(app: Flask)->None:
    """Register Flask extensions."""

    return None


def register_blueprints(app: Flask)->None:
    """Register Flask blueprints."""

    return None


def register_shellcontext(app: Flask)->None:
    """Register shell context objects."""
    def shell_context()->dict:
        """Shell context objects."""
        return {
        }

    app.shell_context_processor(shell_context)

def register_commands(app: Flask)->None:
    """Register Click commands."""
    return None
    