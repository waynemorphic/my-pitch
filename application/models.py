from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

# class User():
#     '''
#     class contains the user details
#     '''
    
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password
        
# class Comment:
#     '''
#     class defines the comment section of the pitch
#     '''
    
#     all_comments = []
    
#     def __init__(self, username, profile_picture, pitch, upvote, downvote, pitch_date, feedback):
#         self.username = username
#         self.profile_picture = profile_picture
#         self.pitch = pitch
#         self.upvote = upvote
#         self.downvote = downvote
#         self.pitch_date = pitch_date
#         self.feedback = feedback
        
#     def save_comment(self):
#         Comment.all_comments.append(self)
        
#     @classmethod
#     def clear_comment(cls):
#         Comment.all_comments.clear()
  
# database classes and cases      
class Users(db.Model, UserMixin):
    '''
    class contains the users details defined in the database
    '''
    
    # database table
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    image_file = db.Column(db.String(20), default = 'default.jpeg')
    pass_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'author', lazy = 'joined') # referencing the Pitch class
    
    # save the user
    def save_users(self):
        db.session.add(self)
        db.session.commit()
    
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
        return f"Users ({self.username }, { self.email}, {self.image_file})"
    
class Pitch(db.Model):
    '''
    class defines the user pitch posted in the platform
    '''
    
    __tablename__ = 'pitch'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    pitch = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) # referencing the table name users and the column name id
    category_id = db.Column(db.Integer, db.ForeignKey('category.id')) # relationship between pitch and its category
    
    # saving the pitch
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f'Users {self.title}, {self.pitch}, {self.date_posted}, {self.upvote}, {self.downvote}'

class Comment(db.Model):
    '''
    class defines the comment/feedback made on a pitch by other users
    '''
    
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)
    feedback = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    
    # saving the comment
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f"Comment {self.feedback}"
    
class Category(db.Model):
    '''
    class defines the pitch category
    '''
    
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key = True)
    the_category = db.Column(db.String(255))
    pitch_relationsip = db.relationship('Pitch', backref = 'specified_category' , lazy = True) # one category can have many pitches
    
    