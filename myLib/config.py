#config.py
import os
import time
from sikuli.Sikuli import *

def get_img_path():
    """Set up the path to the os specific image directory and for setBundlePath().

    """
    proj_dir = os.path.join(os.getenv("PCF_TEST_HOME"),"MVC")
    img_dir = "Images_"+get_os_name()
    img_path = os.path.join(proj_dir,img_dir)
    return img_path


def set_image_dirs():
    """Set the Sikuli image path for the os specific image directory and the main Image dir.

    """
    dir_list = []
    proj_dir = os.path.join(os.getenv("PCF_TEST_HOME"),"MVC")
    os_image_dir = get_img_path()
    #Add the os-specific image directory to the sikuli search path if it is not in there already   
    if os_image_dir not in list(getImagePath()):
        addImagePath(os_image_dir)
       
def get_os_name():
    """Returns the os string for the SUT
    """
    if "MAC" in str(Env.getOS()):
        return "osx"
    elif "WINDOWS" in str(Env.getOS()):
        return "win"
    elif "LINUX" in str(Env.getOS()):
        return "lin"
    else:
        print ("I don't know how to handle platform '%s'", Env.getOS())


def launch_cmd():
    """Returns the launch path for the application.

    launch is an os specific command
    """
    if get_os_name() == "osx":
        launch_cmd =  "/Applications/MVC.app"
    elif get_os_name() == "win":
        launch_cmd = os.path.join(os.getenv("PROGRAMFILES"),"Participatory Culture Foundation","Miro Video Converter","MiroConverter.exe")
    else:
        print get_os_name()
    print launch_cmd
    return launch_cmd





    

    
