#mvclib.py
import os
import shutil
import time
import glob
import time
import glob
import config
import testvars
from sikuli.Sikuli import *
import glob



INPUT_DIR = os.path.join(os.path.join(os.getenv("PCF_TEST_HOME"),"MVC", "TestData"))

def input_files():
    testfiles = []
    for testfile in glob.glob( os.path.join(INPUT_DIR, '*.*') ):
        testfiles.append(os.path.basename(testfile))
    print testfiles
    return testfiles

def set_regions():
    config.set_image_dirs()
    wait(Pattern("top_app.png"), 20)
    mvc = Region(getLastMatch())
    mvc.setH(mvc.getH()+650)
    return mvc


class MVCApp(object):

    def __init__(self):
        self.os_name = config.get_os_name()
        self.mvcapp = App(config.launch_cmd())
        self.testfiles = input_files()
        self.DEVICE_MENU = Pattern("device_menu.png")       
        self.CONVERT = Pattern("convert.png")
        self.DROP_ZONE = Pattern("drop_zone.png")
        self.CHOOSE_FILE = Pattern("choose_a_file.png")
        self.STARTING = Pattern('starting.png')
        self.FINISHED = Pattern('finished.png')
        self.OPEN = Pattern('Open.png')
        self.mvcapp.focus()
        time.sleep(3)
        self.reg = set_regions()
        setAutoWaitTimeout(10)
    
    def _choose_format(self, out_format):
        if self.reg.exists(out_format):
            return
        self.reg.click(self.DEVICE_MENU)
        if config.get_os_name() == "win":
            if out_format == "iPad":
                type("i")
                type(Key.ENTER)
            elif out_format == "Nano":
                type("i")
                for x in range(0,3):
                    type(Key.DOWN)
                type(Key.ENTER)
            elif out_format == "MP3":
                type("m")
                type(Key.DOWN)
                type(Key.ENTER)
            elif out_format == "MP4":
                type("m")
                type(Key.ENTER)
            elif out_format == "PSP":
                type("p")
                type(Key.ENTER)
            elif out_format == "Hero":
                type("h")
                type(Key.ENTER)
            elif out_format == "Cliq":
                type("c")
                type(Key.ENTER)
            elif out_format == "G1":
                type("g")
                type(Key.ENTER)
            elif out_format == "WebM":
                type("w")
                type(Key.ENTER)
            elif self.reg.exists(out_format):
                click(self.reg.getLastMatch())
            else:
                raise Exception("Output format not found")
        else:
            self.reg.click(out_format)
            

    def _add_a_file(self, filename):
        input_file_path = os.path.join(os.path.join(os.getenv("PCF_TEST_HOME"),"MVC", "TestData"))
        testfile = os.path.join(input_file_path, filename)
        self.reg.click(self.CHOOSE_FILE)
        time.sleep(2)
        type(testfile +"\n")
        if config.get_os_name() == "osx":
            time.sleep(2)
            type(Key.ENTER)
            
            
    
    def _convert_file(self):
        self.reg.wait(self.CONVERT, 5)
        self.reg.click(self.CONVERT)
        try:
            waitVanish(self.STARTING, 15)
        except:
            print "Stuck in starting, cancelling failed conversion"
            self.reg.click("Cancel")
            return False
        try:
            wait(self.FINISHED, 1500)
        except:
            raise Exception("Conversion not finished after 5 minutes")

    def output_files_exist(self, converted_files):
        output_file_dir = os.path.join(os.path.join(os.getenv("PCF_TEST_HOME"),"MVC", "OutputFiles"))
        file_errors = []
        for f in converted_files:
            if os.path.isfile(f):
                exists =  True
                shutil.copy(f, output_file_dir)
                os.unlink(f)
            else:
                file_errors.append("Output file %s does not exist" % f)
        return file_errors


    def do_conversions(self, conversion, extension):
        output_files = []   
        for testfile in self.testfiles:
            print testfile
            self._choose_format(conversion)
            self._add_a_file(testfile)
            self._convert_file()
            fileparts = testfile.split('.')
            fileparts.pop(-1)
            fileparts.append(extension)
            converted_filename = ".".join(fileparts)
            outfile = os.path.join(INPUT_DIR, converted_filename)
            output_files.append(outfile)
            time.sleep(3)
        return output_files

    def close_mvc(self):
        self.mvcapp.close()

    def itunes_off(self):
        """Turn off send to itunes.

        """
        if (exists("send_to_itunes_checked.png")):
            click("send_to_itunes_checked.png")
   

            
