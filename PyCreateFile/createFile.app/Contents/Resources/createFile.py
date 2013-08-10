## This program is designed to simplify the file creation process.
##(C) <2013>  <Colin Murphy>
##
##This program is free software: you can redistribute it and/or modify
##it under the terms of the GNU General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.
##
##You should have received a copy of the GNU General Public License
##along with this program.  If not, see <http://www.gnu.org/licenses/>.

#IMPORTANT: For some reason the program WILL NOT RUN without a config.txt file in the same directory as this. I think it has something to do with try: and except:
import wx
import os

class FileMain(wx.Frame):
    def __init__(self, parent, id):
        try:
            f = open('conf.txt', 'r')
            lines = f.readlines()
            tryFrame = wx.Frame.__init__(self, parent, id, "File Creator", size=(375, 175))
            panel = wx.Panel(self)
            ConfigureButton = wx.Button(panel, label = "Configure", pos = (200, 0), size = (175,100))
            self.Bind(wx.EVT_BUTTON, self.Configure, ConfigureButton)
            LeftCreateFile = wx.Button(panel, label = "Create a file in " + lines[1] , pos = (0, 0), size = (200, 75))
            self.Bind(wx.EVT_BUTTON, self.LeftCreateFile, LeftCreateFile)
            RightCreateFile = wx.Button(panel, label = "Create a file in " + lines[3], pos = (0, 75), size = (200, 75))
            self.Bind(wx.EVT_BUTTON, self.RightCreateFile, RightCreateFile)
            
            LicenseButton = wx.Button(panel, label = "License", pos = (200, 75), size = (175, 75))
            self.Bind(wx.EVT_BUTTON, self.License, LicenseButton)
        except:
            exceptFrame = wx.Frame.__init__(self, parent, id, "File Creator", size=(400, 150))
            panel = wx.Panel(self)
            ConfigureButton = wx.Button(panel, label = "Configure", pos = (200, 0), size = (200,200))
            self.Bind(wx.EVT_BUTTON, self.Configure, ConfigureButton)
            LicenseButton = wx.Button(panel, label = "License", pos = (200, 75), size = (200, 200))
            self.Bind(wx.EVT_BUTTON, self.License, LicenseButton)
            
            
        


    def Configure(self, event):
        '''Sets up the configuration file "config.txt" to point to user defined directorys'''
        configure1 = wx.DirDialog(None)
        if configure1.ShowModal()==wx.ID_OK:
            print configure1
            path = configure1.GetPath()
            path = str(path)
            print path
            f = open('conf.txt', 'w+')
            f.write(path + "/") #this '/' needs to be removable for users on Windows systems.
            f.write("\n")
        location = wx.TextEntryDialog(None, "What do you want to call this location?", "Location", "")
        if location.ShowModal()==wx.ID_OK:
            location = location.GetValue()
            location = str(location)
            f.write(location)
            f.write("\n")
        
        configure2 = wx.DirDialog(None)
        if configure2.ShowModal()==wx.ID_OK:
            path = configure2.GetPath()
            path = str(path)
            print path
            f.write(path + "/")
            f.write("\n")
        location2 = wx.TextEntryDialog(None, "What do you want to call this location?", "Location", "")
        if location2.ShowModal()==wx.ID_OK:
            location2 = location2.GetValue()
            location2 = str(location2)
            f.write(location2)
            f.write("\n")
            f.close()
            self.Destroy()
    def LeftCreateFile(self, event):
        ''' creates a file from the button on top '''
        FileName = wx.TextEntryDialog(None, "what do you want to call this file?", "File Creator", "example.txt")
        FileName.ShowModal()
        Input = FileName.GetValue()
        f = open('conf.txt', 'r')
        lines = f.readlines()
        newFile = open(lines[0].rstrip() + Input, 'w+') #rstrip is required to strip \n from the EOL
        f.close()
        newFile.close
        raise SystemExit
        os._exit
        
    def RightCreateFile(self, event):
        ''' creates a file from the button on bottom '''
        NextFileName = wx.TextEntryDialog(None, "what do you want to call this file?", "File Creator", "example.txt")
        NextFileName.ShowModal()
        Input = NextFileName.GetValue()
        f = open('conf.txt', 'r')
        lines = f.readlines()
        newFile = open(lines[2].rstrip() + Input, 'w+') #rstrip is required to strip \n from the EOL
        f.close()
        newFile.close
        raise SystemExit
        os._exit
        
    def License(self, event):
        box = wx.MessageDialog(None, "This program is Licensed under the GNU GPLv3. By using this software, you agree to the terms of the GPL", "License", wx.OK)
        box.ShowModal()
        

if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=FileMain(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
    
#I dont know which one of these actually exit the program, but I dont want to test it at the moment.
raise SystemExit
os._exit





#/Users/colin/Desktop
