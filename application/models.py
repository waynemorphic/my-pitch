from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class User():
    '''
    class contains the user details
    '''
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
class Comment:
    '''
    class defines the comment section of the pitch
    '''
    
    all_comments = []
    
    def __init__(self, username, profile_picture, pitch, upvote, downvote, pitch_date, feedback):
        self.username = username
        self.profile_picture = profile_picture
        self.pitch = pitch
        self.upvote = upvote
        self.downvote = downvote
        self.pitch_date = pitch_date
        self.feedback = feedback
        
    def save_comment(self):
        Comment.all_comments.append(self)
        
    @classmethod
    def clear_comment(cls):
        Comment.all_comments.clear()
  
# database classes and cases      
class Users(db.Model, UserMixin):
    '''
    class contains the users details defined in the database
    '''
    
    # database table
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_hash = db.Column(db.String(255))
    
    # login
    @property # write only class property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password)    :
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
    
    # querying database for specific user
    @login_manager.user_loader # modifies load_user function
    def load_user(user_id):
        return Users.query.get(int(user_id))
    
    def __repr__(self):
        return f'Users { self.email}'
    
class Role(db.Model):
    '''
    class defines the roles of the users in the application
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('Users',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'Users {self.name}'