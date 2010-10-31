import sys
import os
import glob
import unittest
import StringIO


mycwd = os.path.join(os.getcwd(),"MVC")
sys.path.append(os.path.join(mycwd,'myLib'))
import config
import mvclib

setBundlePath(config.get_img_path())


class apple_devices(unittest.TestCase):
    """Verifies conversions for Apple devices.

    Currently tested devices: ipad, iphone, ipod_classic, ipod_nano
    ipod_touch
    """
    def setUp(self):
        self.verificationErrors = []
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
        self.assertEqual([], self.verificationErrors)
    

suite = unittest.TestLoader().loadTestsFromTestCase(apple_devices)

testlitmus = True
        # Post the output directly to Litmus
if testlitmus == True:
    buf = StringIO.StringIO()
    runner = unittest.TextTestRunner(stream=buf)
    for x in suite:
        runner.run(x)
        # check out the output
        byte_output = buf.getvalue()
        id_string = str(x)
        stat = byte_output[0]
        try:
            print "*** the printed output:"
            print byte_output
            print stat
##                litmusresult.write_log(id_string,stat,testbuildid,byte_output)
##                litmusresult.send_result()
        finally:
            buf.truncate(0)



#unittest.TextTestRunner().run(suite)
