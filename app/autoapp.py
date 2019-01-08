"""Create an application instance."""
from app.api.app import create_app
from app.api.extensions import CFG

APP = create_app(CFG)
