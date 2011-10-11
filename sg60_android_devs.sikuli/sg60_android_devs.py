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
    """Verifies conversions for Android devices.

    Currently tested devices: behold, nexus one, Magic, Hero,
    G1 / Dream, Eris/Desire, Droid, Cliq /DEXT
    """


    def test_353(self):
        mvc = mvclib.MVCApp()
        conversion = "Behold"
        extension = "behold.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])
        

    def test_360(self):
        mvc = mvclib.MVCApp()
        conversion = "Nexus"
        extension = "nexusone.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])  
        
        
    def test_359(self):
        mvc = mvclib.MVCApp()
        conversion = "magic"
        extension = "magic.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])        
        

    def test_358(self):
        """Hero conversions.

        """
        mvc = mvclib.MVCApp()
        conversion = "Hero"
        extension = "hero.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])


    def test_357(self):
        mvc = mvclib.MVCApp()
        conversion = "G1"
        extension = "g1.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])
          

    def test_356(self):
        """Eris / Desire
        """
        mvc = mvclib.MVCApp()
        conversion = "Desire"
        extension = "eris.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])


    def test_355(self):
        """Droid Conversions.

        """
        mvc = mvclib.MVCApp()
        conversion = "Droid"
        extension = "droid.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])
     

    def test_354(self):
        """Cliq / DEXT

        """
        mvc = mvclib.MVCApp()
        conversion = "Cliq"
        extension = "cliq.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])

    
# Post the output directly to Litmus
if __name__ == "__main__":
    import LitmusTestRunner
    print len(sys.argv)
    if len(sys.argv) > 1:
        LitmusTestRunner.LitmusRunner(sys.argv, ).litmus_test_run()
    else:
        LitmusTestRunner.LitmusRunner(MVC_Suite, ).litmus_test_run()



