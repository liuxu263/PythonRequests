# coding:utf-8
from python_requests.testcases.testcase1 import TestCase1
from python_requests.testcases.testcase2 import TestCase2
import unittest


class TestSuite1(object):
    suite = unittest.TestSuite()
    test1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    test2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    suite.addTest(test1)
    suite.addTest(test2)
