import unittest

from guess import Guess

class TestGuess(unittest.TestCase):
    
    def setUp(self):
        self.g1 = Guess('default')
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()