import os
import pywinauto
import time
from time import sleep
import sys
import datetime
import logging
import os
import pyautogui
from pywinauto import application
import subprocess
import PIL
from subprocess import Popen
import webbrowser

# 1st way
#path = 'C:\Automation\TestFileForDigital.html'
#webbrowser.open_new_tab(path)
# 2nd way
subprocess.run(["explorer", "C:\Automation\TestFileForDigital.html"])
# 3rd way
#os.system("C:\Automation\TestFileForDigital.html")
#os.startfile("C:\Automation\TestFileForDigital.html")
#output_html_path=os.getcwd()+"//"+"C:\Automation\TestFileForDigital.html"


time.sleep(5)


screenshot = pyautogui.screenshot()
screenshot.save('C:\Automation\image2.png')



#os.system("cls")

#print("\u001b[42m\u001b[31hello \u001b[34mworld\u001b[37m\u001b[40m")
#print("\033[31m"+"this is Ajay")


#class Colours:
    #grey = '\033[90m'
   # red = '\033[91m'
    #green = '\033[92m'

#print(Colours.red+'Hello world')
