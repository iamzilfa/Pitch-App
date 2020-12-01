import unittest
from app.models import Comment, Pitch
from app import db

class TestPitchComment(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(post = "wow", category='sport')
        self.new_comment = Comment(comment = "Thanks for your feedback", pitch=self.new_pitch)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,"Thanks for your feedback")
        self.assertEquals(self.new_comment.pitch,self.new_pitch,'wow')