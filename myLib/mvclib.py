#mvclib.py

import os
import time
import glob
import config
from sikuli.Sikuli import *

setBundlePath(config.get_img_path())


def convert_files(self,testfile,device):
    """Convert a file to the specified device.

    """
    print "converting to " +device+ ": "+os.path.basename(testfile)
    wait("choose_file.png",20)
    click("choose_file.png")
    filename = os.path.basename(testfile)
    fn = filename.split('.')
    wait("search_box.png",15)
    type("search_box.png",fn[0])
    fileimg = "I"+filename+".png"
    wait(fileimg,45)
    self.assertTrue(exists(fileimg))
    click(fileimg)
    click("open.png")
    wait("convert_active.png",15)
    click("convert_active.png")
    if wait_finished_converting(self) == "Error":
        self.verificationErrors.append(filename +" failed to convert")
        
    

def itunes_off(self):
    """Turn off send to itunes.

    """
    if (exists("send_to_itunes_checked.png")):
        click("send_to_itunes_checked.png")


def cclick(self,img,ddir=getBundlePath()):
    """Look through the image dir and click any image that matches the given name.

    """                                    
    for image in glob.glob( os.path.join(ddir, img+'*.png')):
        print image
        if exists(image):
            click(image)
            break

    
        
def wait_finished_converting(self):
    """Wait for conversion to finish, or capture error.

    """
    status = "Pass"
    while not exists("finished_converting.png"):
        if exists("conversion_failed.png"):
            print "conversion failed"
            status = "Error"
            cclick(self,"ok")
            break
        elif exists("ready_to_convert.png"):
            break
        else:
            time.sleep(3)
    return status
            
