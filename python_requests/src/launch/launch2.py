#! /user/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import unittest

from python_requests.src.testsuites.testsuite2 import TestSuite2
from python_requests.src.common.utils import set_env

if __name__ == '__main__':
    file_path = os.path.abspath(os.path.dirname(__file__)) + "/python_requests/testdata/config"
    set_env(file_path, sys.argv[1])
    suite = TestSuite2().suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
