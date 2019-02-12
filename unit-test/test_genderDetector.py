import unittest
from genderDetector.genderDetector import GenderDetector


class GenderDetectorTest(unittest.TestCase):

    def setUp(self):
        self.detector = GenderDetector()

    def test_should_return_female_when_the_name_is_from_female_gender(self):
        gender = self.detector.run('Ana')
        assert gender == 'female'

    def test_should_return_male_when_the_name_is_from_male_gender(self):
        gender = self.detector.run('Pedro')
        assert gender == 'male'


if __name__ == '__main__':
    unittest.main()