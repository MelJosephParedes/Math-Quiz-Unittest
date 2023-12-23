import unittest
from io import StringIO
import sys

from main import generate_numbers, math_quiz, select_operator, number_of_items, max_difference, settings

class TestMathQuiz(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.level = 1
        cls.operator = '+'
        cls.num_items = 5
        cls.max_diff = 5

    def test_generate_numbers_level_1(self):
        result = generate_numbers(1)
        self.assertTrue(1 <= result[0] <= 10)
        self.assertTrue(1 <= result[1] <= 10)

    def test_generate_numbers_level_2(self):
        result = generate_numbers(2)
        self.assertTrue(11 <= result[0] <= 100)
        self.assertTrue(11 <= result[1] <= 100)
    
    def test_select_operator(self):
        # Redirect stdout to capture user input
        sys.stdout = StringIO()
        sys.stdin = StringIO('+\n')
        self.assertEqual(select_operator(), '+')
        # Reset redirect
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_number_of_items(self):
        sys.stdout = StringIO()
        sys.stdin = StringIO('5\n')
        self.assertEqual(number_of_items(), 5)
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_max_difference(self):
        sys.stdout = StringIO()
        sys.stdin = StringIO('5\n')
        self.assertEqual(max_difference(), 5)
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_settings(self):
        sys.stdout = StringIO()
        sys.stdin = StringIO('2\n-\n3\n5\n')
        try:
            settings()
        except EOFError as e:
            self.fail(f"An EOFError occurred: {e}")
        finally:
            sys.stdout = sys.__stdout__
            sys.stdin = sys.__stdin__

        self.assertEqual(self.level, 1)
        self.assertEqual(self.operator, '+')
        self.assertEqual(self.num_items, 5)
        self.assertEqual(self.max_diff, 5)

        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_math_quiz(self):
        sys.stdout = StringIO()
        sys.stdin = StringIO('1\n')
        try:
            math_quiz()
            math_quiz_output = sys.stdout.getvalue()
            self.assertTrue("Correct Answer:" in math_quiz_output)
            self.assertTrue("Wrong answers:" in math_quiz_output)
        except EOFError as e:
            self.fail(f"An EOFError occurred: {e}")
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

if __name__ == '__main__':
    unittest.main()