''' This is the settings file responsible for every parameter on this APP.
All parameters MUST be here in order to keep things with good maintainability
'''

from decouple import config

class Config(): # pylint: disable=too-few-public-methods
    """Main class Config that holds all the Production configuration
    """

    #App Conf
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config('SECRET_KEY',
                        default='.?m]GJ@L9vA>Te6q;<iA:jTm{=?JwqV_@>+ewNyCXxcH//8Mq7zOYUeFT3<jv{@E')


class ProdConfig(Config): # pylint: disable=too-few-public-methods
    """Production Config

    Inherits from Config class and overwrites some parameters
    """
    DEBUG = False
    FLASK_ENV = 'production'
    ENV = 'production'


class DevConfig(Config): # pylint: disable=too-few-public-methods
    """Development Config

    Inherits from Config class and overwrites some parameters
    """
    FLASK_ENV = 'development'
    ENV = 'development'
    DEBUG = True

class StageConfig(Config): # pylint: disable=too-few-public-methods
    """Stage Config

    Inherits from Config class and overwrites some parameters
    """
    FLASK_ENV = 'production'
    ENV = 'stage'
    DEBUG = True


class TestConfig(Config): # pylint: disable=too-few-public-methods
    """Test Config

    This is a special class that inherits from Config class
                          and overwrites some parameters for tests
    """
    ENV = 'test'

def config_to_class(environ_class: str)->Config:
    """A function that returns the desired configuration class based on environ var

    Arguments:
        environ_class {str} -- An environ var used to configure the app

    Returns:
        Config -- A class that represents the appropriate environment
    """
    class_dict = {
        'development': DevConfig(),
        'production': ProdConfig(),
        'test': TestConfig(),
    }
    return class_dict[environ_class]
