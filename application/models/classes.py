import profile


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
    
    def __init__(self, username, profile_picture, pitch, upvote, downvote, pitch_date, feedback):
        self.username = username
        self.profile_picture = profile_picture
        self.pitch = pitch
        self.upvote = upvote
        self.downvote = downvote
        self.pitch_date = pitch_date
        self.feedback = feedback