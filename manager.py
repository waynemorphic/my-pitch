from flask import Flask
from flask_bootstrap import Bootstrap
from application import create_app, db
from flask_script import Manager, Server
from application.models import Users, Pitch
from  flask_migrate import Migrate
from flask_migrate import MigrateCommand # pip install flask_migrate==2.6.0

# app instance
app = create_app('production')
# app = create_app('test')

# instantiating the Manager class
manager = Manager(app)

# add_command runs the server
manager.add_command('server', Server)

# initializing flask_migrate
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

# running unittests
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# shell context
@manager.shell
def make_shell_context()   :
    return dict (app = app, db = db, Users = Users, Pitch = Pitch)

# running the application
if __name__ == '__main__':
    manager.run()