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
    """Verifies conversions for Android devices.

    Currently tested devices: behold, nexus one, Magic, Hero,
    G1 / Dream, Eris/Desire, Droid, Cliq /DEXT
    """
    def setUp(self):
        self.verificationErrors = []
        setAutoWaitTimeout(60)
        switchApp(config.get_launch_cmd())
        wait("device_menu.png")


    def test_353(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "behold"
        click(device+".png")
        mvclib.itunes_off(self)
        d = {}
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)

    def test_360(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "nexus_one"
        click(device+".png")
        mvclib.itunes_off(self)
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)
        
    def test_359(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "magic"
        click(device+".png")
        mvclib.itunes_off(self)
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)
        
        

    def test_358(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "hero"
        mvclib.itunes_off(self)
        click(device+".png")
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)   


    def test_357(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "dream"
        mvclib.itunes_off(self)
        click(device+".png")
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)

    def test_356(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "eris"
        mvclib.itunes_off(self)
        click(device+".png")
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)

    def test_355(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "droid"
        mvclib.itunes_off(self)
        click(device+".png")
        for testfile in glob.glob( os.path.join(path, '*.*') ):
            mvclib.convert_files(self,testfile,device)

    def test_354(self):
        path = os.path.join(mycwd,"TestInput")
        click("device_menu.png")
        device = "cliq"
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

