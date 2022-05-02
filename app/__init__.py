from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


#initializing extensions
bootstrap = Bootstrap()


def create_app(config_name):
    web = Flask(__name__)
    # Set up configuration
    web.config.from_object(config_options[config_name])
    
     # Registering the blueprint
    from .main import main as main_blueprint
    web.register_blueprint(main_blueprint)

    # Initializing flask extensions
    bootstrap.init_app(web)
    
    #  setting config
    from .requests import configure_request
    configure_request(web)

    return web