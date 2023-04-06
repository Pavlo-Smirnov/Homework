import unittest
import example_functions

class MathTestCase(unittest.TestCase):


    def test_some_addition(self):
        result = example_functions.some_addition()
        prediction = 14
        self.assertEqual(result, prediction)

    def test_some_subtracting(self):
        result = example_functions.some_subtracting()
        prediction = 30
        self.assertEqual(result, prediction)

    def test_some_multiplication(self):
        result = example_functions.some_multiplication()
        prediction = 41
        self.assertNotEqual(result, prediction)



if __name__ == "__main__":
    unittest.main()