# coding:utf-8
import sys
import os

sys.path.append('../')
from python_requests.testsuites.testsuite1 import TestSuite1
from python_requests.common.utils import set_env
import unittest

if __name__ == '__main__':
    file_path = os.path.abspath(os.path.dirname(os.getcwd())) + "/python_requests/testdatas/config"
    set_env(file_path, sys.argv[1])
    suite = TestSuite1().suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
