from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from .config import config_options
from flask_sqlalchemy import SQLAlchemy 

# extensions initialization
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    
    # creating app configurations
    app.config.from_object(config_options[config_name])
    
    # flask extension initialization
    bootstrap.init_app(app)
    db.init_app(app)
    
    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app



# from application.main import views
# from application.main import error