from Helloworld import square

import unittest

class SquareTestCase(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(square(5), 25)
    
    def test_negative_number(self):
        self.assertEqual(square(-3), 9)
    
    def test_zero(self):
        self.assertEqual(square(0), 0)

if __name__ == '__main__':
    # Run the tests and collect the results
    test_suite = unittest.TestLoader().loadTestsFromTestCase(SquareTestCase)
    test_result = unittest.TextTestRunner().run(test_suite)

    # Print the number of tests that passed and failed
    passed = len(test_result.successes)
    failed = len(test_result.failures)
    print(f"Tests passed: {passed}")
    print(f"Tests failed: {failed}")

