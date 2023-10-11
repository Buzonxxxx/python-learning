# python3 -m unittest -v

import unittest
import guess_number

class TestGame(unittest.TestCase):

    def test_input(self):
        guess = 10
        answer = 10
        result = guess_number.run_guess_game(guess,answer)
        self.assertTrue(result)
    
    def test_input_wrong_guess(self):
        guess = 0
        answer = 5
        result = guess_number.run_guess_game(guess,answer)
        self.assertFalse(result)
    
    def test_input_out_of_bound(self):
        guess = 11
        answer = 15
        result = guess_number.run_guess_game(guess,answer)
        self.assertFalse(result)
    
    def test_input_wrong_type(self):
        guess = '11'
        answer = 5
        result = guess_number.run_guess_game(guess,answer)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()


