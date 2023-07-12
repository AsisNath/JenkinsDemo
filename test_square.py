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
    test_runner = unittest.TextTestRunner()
    test_result = test_runner.run(test_suite)

    # Count the number of tests that passed and failed
    passed = test_result.wasSuccessful()
    failed = len(test_result.errors) + len(test_result.failures)

    # Print the number of tests that passed and failed
    print(f"Tests passed: {passed}")
    print(f"Tests failed: {failed}")


