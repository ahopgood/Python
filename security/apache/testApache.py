__author__ = 'Alexander'
import unittest
import apache
class TestApache(unittest.TestCase):

    def test_live_givenInvalidUrl(self):
        self.assertEqual(-1, apache.checkStaticPage("http://wwww.google.co.uk/"))

    def test_live_givenValidUrl(self):
        self.assertEqual(200, apache.checkStaticPage("http://www.google.co.uk/"))

if __name__ == '__main__':
    unittest.main()