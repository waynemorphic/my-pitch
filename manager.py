from flask import Flask
from flask_bootstrap import Bootstrap
from application import create_app
from flask_script import Manager, Server

# app instance
app = create_app('development')

# instantiating the Manager class
manager = Manager(app)

# add_command runs the server
manager.add_command('server', Server)

# running the application
if __name__ == '__main__':
    manager.run()