import pywinauto
import time
import subprocess
from subprocess import Popen

#Keyword-LaunchVRNI
app = pywinauto.application.Application(backend = "uia")
app = app.start("C:\Ovation\OvationBase\OvVirtualRNIConfigMgr.exe")
app.OvationVirtualRNIConfigurationManager.wait('ready', timeout = 3000)
app.OvationVirtualRNIConfigurationManager.set_focus()


app.OvationVirtualRNIConfigurationManager.print_control_identifiers()

app.OvationVirtualRNIConfigurationManager.child_window(title="Connect", control_type="Button").click()


