
class User:
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