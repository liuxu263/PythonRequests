#! /user/bin/env python
# -*- coding:utf-8 -*-

import unittest

from python_requests.src.testcases.testcase1 import TestCase1
from python_requests.src.testcases.testcase2 import TestCase2


class TestSuite1(object):
    suite = unittest.TestSuite()
    test1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    test2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    suite.addTest(test1)
    suite.addTest(test2)
