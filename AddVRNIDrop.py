import pywinauto
import time
import subprocess
from subprocess import Popen

#Keyword-LaunchVRNI
app = pywinauto.application.Application(backend = "uia")
app = app.start("C:\Ovation\OvationBase\OvVirtualRNIConfigMgr.exe")
app.OvationVirtualRNIConfigurationManager.wait('ready', timeout = 3000)
app.OvationVirtualRNIConfigurationManager.set_focus()



#Keyword-LaunchVRNI
    #add "IP address"
dlg1 = app.OvationVirtualRNIConfigurationManager
dlg2 = dlg1.child_window(title="192.168.104.211", control_type="Edit")

dlg1 = app.OvationVirtualRNIConfigurationManager

dlg2 = dlg1.child_window(title="192.168.104.211", control_type="Edit")
dlg2.type_keys("192.168.104.211"+"{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}")
    #To Press "Connect"
dlg2.type_keys("{TAB}{ENTER}")

 #Keyword- addVRNI Drop
#app.Dialog.print_control_identifiers()
dlg4 = dlg1.child_window(title="Ovation Drops", control_type="TreeItem")
dlg4.select()
dlg4.type_keys("{TAB}{TAB}{SPACE}")



dlg5 = dlg1.child_window(title="New Drop", control_type="Edit")
dlg5.select()
dlg5.select().click_input(button='left')
dlg5.type_keys("{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}"+"Drop6"+"{TAB}{DELETE}"+"6"+"{TAB}"+"192.168.104.6"+"{TAB}{TAB}{TAB}{ENTER}"+"{TAB}{ENTER}")

#Keyword Inject Digital value,Drop6TreeItem1

Test = app.OvationVirtualRNIConfigurationManager.Drop6.select()
app.OvationVirtualRNIConfigurationManager.print_control_identifiers()
