import unittest
import test_case_one

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = test_case_one.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = test_case_one.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '_main_':
    unittest.main()