"""The app module, containing the app factory function."""

from flask import (Flask, jsonify)

from app.api.settings import (ProdConfig, Config)

def create_app(config_object: Config = ProdConfig)->Flask:
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    Keyword Arguments:
        config_object {Config} -- A configuration object to be used (default: {ProdConfig})

    Returns:
        Flask -- Returns a Flask object
    """

    app = Flask(__name__.split('.')[0], static_url_path='/static', static_folder='static')

    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    register_commands(app)

    register_handlers(app)

    return app


def register_extensions(app: Flask)->None:
    """Register Flask extensions."""

    return None


def register_blueprints(app: Flask)->None:
    """Register Flask blueprints."""

    return None

def register_handlers(app: Flask)->None:
    """Register handlers of app"""

    @app.errorhandler(404)
    def page_not_found(): # pylint: disable=unused-variable
        """Send message to the user with notFound 404 status."""
        message = {
            "err":
                {
                    "msg": "This route is currently not supported. Please refer API documentation."
                }
        }

        resp = jsonify(message)
        resp.status_code = 404
        return resp
    