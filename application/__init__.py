from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# application initialization
app = Flask(__name__, instance_relative_config = True)

# configurations setup
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

# flask extension initialization
bootstrap = Bootstrap(app)

from application import views