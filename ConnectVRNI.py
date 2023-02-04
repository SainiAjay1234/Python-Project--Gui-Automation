import pywinauto
import time
import subprocess
from subprocess import Popen

#Keyword-LaunchVRNI
app = pywinauto.application.Application(backend = "uia")
app = app.start("C:\Ovation\OvationBase\OvVirtualRNIConfigMgr.exe")
app.OvationVirtualRNIConfigurationManager.wait('ready', timeout = 3000)
app.OvationVirtualRNIConfigurationManager.set_focus()


#add "IP address"
dlg1 = app.OvationVirtualRNIConfigurationManager
dlg2 = dlg1.child_window(title="192.168.104.211", control_type="Edit")

dlg1 = app.OvationVirtualRNIConfigurationManager

dlg2 = dlg1.child_window(title="192.168.104.211", control_type="Edit")
dlg2.type_keys("192.168.104.211"+"{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}{DEL}")
#To Press "Connect"
dlg2.type_keys("{TAB}{ENTER}")
#dlg3 = dlg2.type_keys("{TAB}{ENTER}")
time.sleep(2)

app.OvationVirtualRNIConfigurationManager.print_control_identifiers()
