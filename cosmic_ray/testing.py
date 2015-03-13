import unittest


def run_tests(test_dir):
    """Discover and run tests in `test_dir`.

    If the tests pass, this returns `(True, result)`, otherwise it
    returns `(False, result)`.
    """
    suite = unittest.TestLoader().discover(test_dir)
    result = unittest.TestResult()
    suite.run(result)
    return result.wasSuccessful, str(result)
