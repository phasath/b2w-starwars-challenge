"""The app module, containing the app factory function."""

from flask import (Flask, jsonify)
from flask_restful import Api

from app.api.settings import (ProdConfig, Config)
from app.api.extensions import (CFG, mongo)
from app.api.utils.error_messages import error_message

def create_app(config_object: Config = ProdConfig)->Flask:
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    Keyword Arguments:
        config_object {Config} -- A configuration object to be used (default: {ProdConfig})

    Returns:
        Flask -- Returns a Flask object
    """

    app = Flask('B2W Star Wars Challenge')

    app.config.from_object(config_object)
    register_extension(app)

    api = make_restful(app)
    api = register_resource(api)

    register_handlers(app)

    return app

def make_restful(app: Flask)->Api:
    """This converts the Flask app to use Restful resources easily

    Arguments:
        app {Flask} -- The app which 'will become' restful

    Returns:
        api {Api} -- An object of Api Restful class.
    """
    api = Api(app)

    return api

def register_extension(app: Flask)->None:
    """Register APP extensions."""

    mongo.init_app(app=app, uri=CFG.MONGODB_URI)
    

    return None

def register_resource(api: Api)->Api:
    """Register API resource."""

    api.add_resource(Index, "/", endpoint="index")

    return api

def register_handlers(app: Flask)->None:
    """Register handlers of app"""

    @app.errorhandler(404)
    def page_not_found(_e): # pylint: disable=unused-variable, unused-argument
        """Send message to the user with notFound 404 status."""
        return error_message(404, 'This route is currently not supported. Please refer API documentation.')

