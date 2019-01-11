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
    MONGODB_URI = config('MONGODB_URI',
                         default=('mongodb://heroku_xtghhb5l:3jq91uffr61e0jun3fbqfk4ccn@'
                         'ds151354.mlab.com:51354/heroku_xtghhb5l'))
                         
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
    MONGODB_URI = config('MONGODB_URI',
                         default='mongodb://obi_wan:kenobi@127.0.0.1:27017/star_wars_planets')

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
    MONGODB_URI = config('MONGODB_URI', default=
                         ("mongodb://chewbacca:GGGWARRRHHWWWW@"
                          "127.0.0.1:27017/star_wars_planets_test"))


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
