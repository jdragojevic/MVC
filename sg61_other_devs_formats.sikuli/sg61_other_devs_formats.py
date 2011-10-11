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
    """Verifies conversions for Additional devices and formats.

    Currently tested devices and formats: Theora, MP3 (audio only),
    MP4, PSP, WebM
    """   

    def test_351(self):
        mvc = mvclib.MVCApp()
        conversion = "Theora"
        extension = "theora.ogv"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])


    def test_366(self):
        mvc = mvclib.MVCApp()
        conversion = "MP3"
        extension = "audioonly.mp3"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])

        
    def test_367(self):
        mvc = mvclib.MVCApp()
        conversion = "MP4"
        extension = "mp4video.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])        
        
    def test_352(self):
        mvc = mvclib.MVCApp()
        conversion = "PSP"
        extension = "psp.mp4"
        outfiles = mvc.do_conversions(conversion, extension)
        self.assertTrue(mvc.output_files_exist(outfiles) == [])

    def test_webm(self):
        mvc = mvclib.MVCApp()
        conversion = "WebM"
        extension = "webmvp8.webm"
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


