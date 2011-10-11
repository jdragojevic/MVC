import unittest
from sikuli.Sikuli import *

class MVC_unittest_testcase(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        print "starting test: ",self.shortDescription()


    def tearDown(self):
        App.close("Miro Video Converter")
