from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from .config import config_options
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
# from . import views, forms

# extensions initialization
bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)

# login manager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'

def create_app(config_name):
    app = Flask(__name__)
    
    # creating app configurations
    app.config.from_object(config_options[config_name])
    
    # flask extension initialization
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # configure UploadSet
    configure_uploads(app,photos)
    
    return app




# from application.main import error