#config.py


import os
from sikuli.Sikuli import *


def get_img_path():
    """Set up the path to the image directory and for setBundlePath().

    """
    mycwd = os.path.join(os.getcwd(),"MVC")
    setBundlePath(os.path.join(mycwd,'Images_'+testvars.get_os_name()))
    return img_path


def get_os_name():
    """Returns the os string for the SUT
    """
       
    if "MAC" in str(Env.getOS()):
	return "osx"
    else:
        print ("I don't know how to handle platform '%s'", Env.getOS())

def get_launch_cmd():
    """Returns the launch path for the application.

    launch is an os specific command
    """
    if get_os_name() == "osx":
        return "/Applications/Miro Video Converter.app"
    else:
        print "no clue"

    
