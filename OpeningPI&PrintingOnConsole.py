import pywinauto
import time
import sys
import logging
import os
import subprocess
from subprocess import Popen

#Opening PI and read value
app = pywinauto.application.Application(backend = "uia")
app = app.start("C:\Ovation\OvationBase\PI.exe")
app.OvationPointInformation.wait('ready', timeout = 30)
app.OvationPointInformation.set_focus()


#setting PI as dialog
time.sleep(5)
dlg = app.OvationPointInformation
#dlg.dump_tree()
dlg1 = dlg.child_window(auto_id="NewPointNameCB", control_type="Pane")
dlg1.click_input()
dlg1.type_keys("ANALOG_A8"+"~")
#dlg.print_control_identifiers()
var1 = dlg.child_window(title="51", control_type="Custom").exists(1)

if var1 == True : print ("ANALOG_A8 value changed to 80")

else:  print ("Test case is failed to change the value")
   # img = dlg.capture_as_image()
   # img.save('PI_screenshot.png')
    
        












#child_window(title="0", control_type="Edit")
#child_window(title="Analog Value: ", control_type="Text")
#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()


#dlg10 = dlg1.child_window(title="Start module...", control_type="Button")
#dlg10.click_input()



#dlg9.type_keys('{TAB 5}{ENTER}')
#child_window(title="Module 2", control_type="TreeItem")

#lg8 = dlg1.child_window(title="Digital Value: ", control_type="Text")
#lg8.select()
#lg8.set_focus().click_input(button='left', double='true',coords=(0, 0))


#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()
#dlg8 = dlg1.child_window(title="Node 1", control_type="TreeItem")
#dlg8.select()
#dlg7.type_keys('{DOWN}'+'+{RIGHT}'+'{TAB}{TAB}{TAB}{TAB}{SPACE}'+'{TAB 7}{DOWN}'+'{TAB 5}{ENTER}'+'{TAB 6}{RIGHT}'+'{DOWN}{RIGHT}{DOWN}'+'{TAB 3}{RIGHT}{TAB}{ENTER}')
#dlg8.set_focus().click_input(button='right', double='true',coords=(60, 5))
#dlg9 = app.OvationVirtualRNIConfigurationManager.child_window(title="Start", control_type="MenuItem").wrapper_object()
#dlg9.click_input()
#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()
#dlg10 = dlg1.child_window(title="Node 1TreeItem", control_type="TreeItem")
#dlg10.type_keys('+{RIGHT}')


#dlg10 = app.OvationVirtualRNIConfigurationManager.child_window(title="Node 1 (Running)", control_type="Button")
#dlg10.type_keys('+{RIGHT}')

#dig7.type_keys("+{RIGHT}")

#dlg9.type_keys('+{RIGHT}')
#dlg10 = app.OvationVirtualRNIConfigurationManager.child_window(title="Node 1 (Running)", control_type="Button").wrapper_object()
#dlg10.type_keys(double='true')

#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()

#item = dlg1.child_window(title="Node 1 (Stopped)", control_type="Text").FolderView.GetItem('Start')
#item.EnsureVisible()
#item.RightClickInput()
#child_window(title="Node 1 (Stopped)", control_type="Text")
#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()
#dlg9 = app.OvationVirtualRNIConfigurationManager.child_window(title="Node 1", control_type="TreeItem").wrapper_object()
#dlg9.MenuSelect("Node 1 -> Start")

#app.OvationVirtualRNIConfigurationManager.Menuselect("Node 1 -> Start")
#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()
#wheel_mouse_input(wheel_dist=10)
#dlg7.type_keys('{DOWN}'+'+{RIGHT}'+'{TAB}{TAB}{TAB}{TAB}{SPACE}'+'{TAB 7}{DOWN}'+'{TAB 5}{ENTER}'+'{TAB 6}{RIGHT}'+'{DOWN}{RIGHT}{DOWN}'+'{TAB 3}{RIGHT}{TAB}{ENTER}')



#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()
#dlg9.start.click(coords=(60, 5))

#dlg9 = dlg8.click_input(button='right', double='true',coords=(60, 5))
#dlg10 = dlg9.click_input(button='down', double='true',coords=(60, 5))
 

#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()


#dlg8.Node1(stopped).click(coords=(0, 0))



#dlg8 = dlg1.child_window(title="Node 1 (Stopped)", control_type="Text")
#dlg8.select()
#pywinauto.mouse.click(button='left', coords=(0, 0))


#dlg8 = dlg1.child_window(title="Node 1 (Stopped)", control_type="Text")
#pywinauto.mouse.right_click(coords=(0, 0))
#dlg8.Node1Stopped.set_focus()
#common_files = app.Node1Stopped.ItemsView.get_item('Common Files')
#common_files.right_click_input()

#dlg8.select()
#dlg8.mouse.right_click_input()



#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()
#dlg8 = dlg1.dlg7.child_window(title="Node 1", control_type="TreeItem")
#dlg8.select()
#dlg8.set_focus().click_input(button='left', double='true',coords=(0, 0))
#dlg8.click_input(button='left')

#dlg8.click_input(double = True )


#dlg8 = dlg1.child_window(title="Node 1", control_type="TreeItem")
#dlg8.Node1.double_click(button='left')



#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()

#app.OvationVirtualRNIConfigurationManager.print_control_identifiers()

#app.OvationVirtualRNIConfigurationManager.Drop6.select()


#dig6 = dig1.child_window(title="Drop6", control_type="TreeItem")
#dig6.select()




#app.OvationVirtualRNIConfigurationManager.child_window(title="Ovation Drops", control_type="TreeItem").EditWrapper.Select()
#dlg1.OvationDrops.click()
#app.OvationVirtualRNIConfigurationManager.RightClick("Ovation Drops")
#dlg1.right_click("Ovation Drops -> AddDrop")

#textEditor = app.OvationVirtualRNIConfigurationManager.child_window(title="192.168.104.211", control_type="Edit").wrapper_object()
#textEditor.type_keys("192.168.104.211")
#time.sleep(1)
#app.OvationVirtualRNIConfigurationManager.connect.click()








