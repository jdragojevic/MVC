import sys
import os
import glob
import unittest
import StringIO
import time

mycwd = os.path.join(os.getcwd(),"MVC")
sys.path.append(os.path.join(mycwd,'myLib'))
import config
import mvclib
import litmusresult



setBundlePath(config.get_img_path())


class MVC_Suite(unittest.TestCase):
    """Verifies conversions for Additional devices and formats.

    Currently tested devices and formats: Theora, MP3 (audio only),
    MP4, PSP
    """
    def setUp(self):
        self.verificationErrors = []
        switchApp(config.get_launch_cmd())     


    def test_351(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "theora"
        click(device+".png")
        mvclib.itunes_off(self)
        d = {}
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)

    def test_366(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "mp3"
        click(device+".png")
        mvclib.itunes_off(self)
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)
        
    def test_367(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "mp4"
        click(device+".png")
        mvclib.itunes_off(self)
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)
        
        

    def test_352(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "psp"
        mvclib.itunes_off(self)
        click(device+".png")
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)   
            
    def tearDown(self):
        switchApp(config.get_launch_cmd())
        type("q", KEY_CMD)
        time.sleep(10)
        self.assertEqual([], self.verificationErrors)
    
# Post the output directly to Litmus

if config.testlitmus == True:
    suite_list = unittest.getTestCaseNames(MVC_Suite,'test')
    suite = unittest.TestSuite()
    for x in suite_list:
        suite.addTest(MVC_Suite(x))

    buf = StringIO.StringIO()
    runner = unittest.TextTestRunner(stream=buf)
    litmusresult.write_header(config.get_os_name())
    for x in suite:
        runner.run(x)
        # check out the output
        byte_output = buf.getvalue()
        id_string = str(x)
        stat = byte_output[0]
        try:
            litmusresult.write_log(id_string,stat,byte_output)
        finally:
            buf.truncate(0)
    litmusresult.write_footer()
#or just run it locally
else:
    unittest.main()

