from sqlalchemy import ForeignKey
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

  
# database classes and cases      
class Users(db.Model, UserMixin):
    '''
    class contains the users details defined in the database
    
    Args:
    username, email, bio, image_file, pass_hash, pitches
    '''
    
    # database table
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    image_file = db.Column(db.String(20), default = 'default.jpeg')
    pass_hash = db.Column(db.String(255))
    posts = db.relationship('Pitch', backref = 'author', lazy = True) # referencing the Pitch class
    comment_stuff = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    upvote = db.relationship('Upvote', backref = 'user', lazy = 'dynamic')
    downvote = db.relationship('Downvote', backref = 'user', lazy = 'dynamic')

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
        self.pass_hash = generate_password_hash(password)
        
        
    def verify_password(self, password):
        return check_password_hash(self.pass_hash, password)
    
    # querying database for specific user
    @login_manager.user_loader # modifies load_user function
    def load_user(user_id):
        return Users.query.get(int(user_id))
    
    def __repr__(self):
        return f"Users ({self.username }, { self.email}, {self.image_file})"
    
class Pitch(db.Model):
    '''
    class defines the user pitch posted in the platform
    
    Args:
        title, content, date_posted, upvote, downvote, category
    '''
    
    __tablename__ = 'pitch'
    id = db.Column(db.Integer, primary_key = True)
    pitch_stuff = db.Column(db.Text)
    category_stuff = db.Column(db.String)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    comment_stuff = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')
    upvote = db.relationship('Upvote', backref = 'upvote', lazy = 'dynamic')
    downvote = db.relationship('Downvote', backref = 'downvote', lazy = 'dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) # referencing the table name users and the column name id
    
    # saving the pitch
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    # getting pitch id
    @classmethod
    def get_pitch_id(cls, id):
        pitch_id = Pitch.query.filter_by(id = id).order_by(Pitch.id.desc())
        return pitch_id
    
    
    @classmethod
    def get_user_pitch(cls):
        users_pitch = Pitch.query.all()
        return users_pitch
    
    # category method
    @classmethod
    def get_pitch_category(cls, id):
        pitch_category = Pitch.query.filter_by(category_id = id).order_by(Pitch.date_posted.desc())
        return pitch_category
    
    
    def __repr__(self):
        return f'Users {self.date_posted}, {self.upvote}, {self.downvote}'

class Comment(db.Model):
    '''
    class defines the comment/feedback made on a pitch by other users
    '''
    
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)
    comment_stuff = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    
    # saving the comment
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    # get comment by pitch
    @classmethod
    def get_comment(cls, id):
        the_comment = Comment.query.filter_by(pitch_id = id).all()
        return the_comment
    
    def __repr__(self):
        return f"Comment {self.comment_stuff}"

class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, ForeignKey('pitch.id'))
    
    def save_upvote(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_upvote(cls, id):
        upvote = Upvote.query.filter_by(pitch_id = id).all()
        return upvote

    def __repr__(self):
        return f" {self.pitch_id} : {self.user_id}"
    
    
class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, ForeignKey('pitch.id'))
    
    def save_downvote(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_downvote(cls, id):
        downvote = Downvote.query.filter_by(pitch_id = id).all()
        return downvote
    
    def __repr__(self):
        return f" {self.pitch_id} : {self.user_id}"
    
    
    
#     '''
#     class defines the pitch category
#     '''
    
#     __tablename__ = 'category'
#     id = db.Column(db.Integer, primary_key = True)
#     the_category = db.Column(db.String(255))
#     pitch_relationsip = db.relationship('Pitch', backref = 'specified_category' , lazy = True) # one category can have many pitches
    
#     # getting category by name
#     @classmethod
#     def get_category_name(cls,the_category):
#         category_name = Category.query.filter_by(the_category = the_category).first()
#         return category_name
    
#     def __repr__(self):
#         return f"Category {self.the_category}"