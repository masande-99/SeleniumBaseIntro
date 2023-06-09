import unittest
import os

if __name__ == '__main__':
    # Set the working directory to the location of the test runner script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)

    # Discover and run the tests
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    runner = unittest.TextTestRunner()
    runner.run(suite)
