import unittest
from application.models import User, Comment


class UserTest(unittest.TestCase):
    '''
    test class to test user class behaviour
    '''
    
    def setUp(self):
        '''
        case runs before every test
        '''
        self.new_user = User('johndoe@gmail.com', 'password')
        
    def test_instance(self):
        '''
        checks if objects belong to the user class
        '''
        
        self.assertTrue(isinstance(self.new_user, User))
        
    def test_init(self):
        '''case checks for proper object initialization
        '''
        
        self.assertEqual(self.new_user.email, 'johndoe@gmail.com')
        self.assertEqual(self.new_user.password, 'password')
        
class CommentTest(unittest.TestCase):
    '''
    class tests comment class behaviour
    '''
    def setUp(self):
        '''
        case runs before every test
        '''
        self.new_comment = Comment('john', 'http://imgurl/profile-picture', 'this is my pitch', '2', '1', 2022-5-5, 'very good work' )
        
    def test_instance(self):
        '''
        checks if objects belong to the comment class
        '''
        
        self.assertTrue(isinstance(self.new_comment, Comment))
        
    def test_init(self):
        '''
        case checks for proper object initialization
        '''
        
        self.assertEqual(self.new_comment.username, 'john') 
        self.assertEqual(self.new_comment.profile_picture, 'http://imgurl/profile-picture' )
        self.assertEqual(self.new_comment.pitch, 'this is my pitch')
        self.assertEqual(self.new_comment.upvote, '2')
        self.assertEqual(self.new_comment.downvote, '1')
        self.assertEqual(self.new_comment.pitch_date, 2022-5-5)
        self.assertEqual(self.new_comment.feedback, 'very good work')

# if __name__ == '__main__':
#     unittest.main()

    
        