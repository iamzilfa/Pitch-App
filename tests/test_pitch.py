import unittest
from app.models import Pitch
Pitch = Pitch

class PitchTest(unittest.TestCase):

    def setUp(self):

        self.new_pitch = Pitch()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))
