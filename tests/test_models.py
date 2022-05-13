import unittest
from application.models import Pitch, Users, Comment


class UsersTest(unittest.TestCase):
    '''
    test class to test user class behaviour
    '''
    
    def setUp(self):
        '''
        case runs before every test
        '''
        self.new_user = Users()
        
    def test_instance(self):
        '''
        checks if objects belong to the user class
        '''
        
        self.assertTrue(isinstance(self.new_user, Users))
        
    def test_init(self):
        '''case checks for proper object initialization
        '''
        
        # self.assertEqual(self.new_user.username)
        # self.assertEqual(self.new_user.email, 'johndoe@gmail.com')
        # self.assertEqual(self.new_user.bio, 'i am who')
        # self.assertEqual(self.new_user.image_file, 'image.jpeg')
        # self.assertEqual(self.new_user.pass_hash, 'password')
        # self.assertEqual(self.new_user.pitches, 'thisiis the pitch')
        
class PitchTest(unittest.TestCase):
    '''
    class tests pitch class behaviour
    '''
    def setUp(self):
        '''
        case runs before every test
        '''
        self.new_pitch = Pitch()
        
    def test_instance(self):
        '''
        checks if objects belong to the pitch class
        '''
        
        self.assertTrue(isinstance(self.new_pitch, Pitch))
        
    def test_init(self):
        '''
        case checks for proper object initialization
        '''
        
        # self.assertEqual(self.new_pitch.user_id) 
        # self.assertEqual(self.new_pitch.title, 'high decibel' )
        # self.assertEqual(self.new_pitch.content, 'this is my pitch')
        # self.assertEqual(self.new_pitch.upvote, '2')
        # self.assertEqual(self.new_pitch.downvote, '1')
        # self.assertEqual(self.new_pitch.date_posted, 2022-5-5)
        # self.assertEqual(self.new_pitch.category_id)

# if __name__ == '__main__':
#     unittest.main()

    
        