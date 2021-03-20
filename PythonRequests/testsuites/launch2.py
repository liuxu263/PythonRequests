from testsuites.testsuite2 import TestSuite2
from common.utils import set_env
import unittest
import sys
import os

if __name__ == '__main__':
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.abspath(os.path.dirname(os.getcwd())) + "/common/config"
    set_env(file_path, sys.argv)
    suite = TestSuite2().suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
