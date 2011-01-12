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
    """Verifies conversions for Apple device+s.

    Currently tested device+s: ipad, iphone, ipod_classic, ipod_nano
    ipod_touch
    """
    def setUp(self):
        self.verificationErrors = []
        setAutoWaitTimeout(60)
        switchApp(config.get_launch_cmd())     


    def test_340(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "iphone"
        click(device+".png")
        mvclib.itunes_off(self)
        d = {}
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)

    def test_341(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "ipod_classic"
        click(device+".png")
        mvclib.itunes_off(self)
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)
        
    def test_342(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "ipod_nano"
        click(device+".png")
        mvclib.itunes_off(self)
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)
        
        

    def test_350(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "ipod_touch"
        mvclib.itunes_off(self)
        click(device+".png")
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)   


    def test_365(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "ipad"
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

