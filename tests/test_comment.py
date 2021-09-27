import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Maxwell = User(first_name = "Maxwell",
                                last_name = "Munene",
                                username = "maxwell_m",
                                password = "kameso1224",
                                email = "maxwell.munene@student.moringaschool.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "Hi!",
                            user_id = self.user_Maxwell.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Maxwell.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Maxwell, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))