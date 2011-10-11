import sys
import os
import unittest
import base_testcase

from sikuli.Sikuli import *
import myLib.config
from myLib import mvclib
from myLib import litmusresult

setBundlePath(myLib.config.get_img_path())

class MVC_Suite(base_testcase.MVC_unittest_testcase):
    """Verifies conversions for Apple device+s.

    Currently tested device+s: ipad, iphone, ipod_classic, ipod_nano
    ipod_touch
    """ 


    def test_340(self):
        """iPhone conversions.

        """
        mvc = mvclib.MVCApp()
        conversion = "iPhone"
        extension = "iphone.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])      
            
    def test_341(self):
        """iPod classic.

        """
        mvc = mvclib.MVCApp()
        conversion = "Classic"
        extension = "ipodclassic.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])  
        
    def test_342(self):
        """iPod nano.

        """
        mvc = mvclib.MVCApp()
        conversion = "Nano"
        extension = "ipodnano.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])  
        
        

    def test_350(self):
        mvc = mvclib.MVCApp()
        conversion = "Touch"
        extension = "ipodtouch.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])  


    def test_365(self):
        mvc = mvclib.MVCApp()
        conversion = "iPad"
        extension = "ipad.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])  

                
# Post the output directly to Litmus

 
# Post the output directly to Litmus
if __name__ == "__main__":
    import LitmusTestRunner
    print len(sys.argv)
    if len(sys.argv) > 1:
        LitmusTestRunner.LitmusRunner(sys.argv, ).litmus_test_run()
    else:
        LitmusTestRunner.LitmusRunner(MVC_Suite, ).litmus_test_run()

