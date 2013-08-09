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
            #f = open(line[2].rstrip() + x , 'w+')
            tryFrame = wx.Frame.__init__(self, parent, id, "File Creator", size=(400, 150))
            panel = wx.Panel(self)
            ConfigureButton = wx.Button(panel, label = "Configure", pos = (200, 0), size = (175,75))
            self.Bind(wx.EVT_BUTTON, self.Configure, ConfigureButton)
            LeftCreateFile = wx.Button(panel, label = "Create a file in " + lines[1] , pos = (0, 0), size = (150, 50))
            self.Bind(wx.EVT_BUTTON, self.LeftCreateFile, LeftCreateFile)
            RightCreateFile = wx.Button(panel, label = "Create a file in " + lines[3], pos = (0,53), size = (150, 50))
            self.Bind(wx.EVT_BUTTON, self.RightCreateFile, RightCreateFile)
            
            DummyButton = wx.Button(panel, label = "other", pos = (200, 35), size = (175, 75))
            self.Bind(wx.EVT_BUTTON, self.DummyPanel, DummyButton)
        except:
            exceptFrame = wx.Frame.__init__(self, parent, id, "File Creator", size=(400, 150))
            panel = wx.Panel(self)
            ConfigureButton = wx.Button(panel, label = "Configure", pos = (200, 0), size = (175,75))
            self.Bind(wx.EVT_BUTTON, self.Configure, ConfigureButton)
            
        


    def Configure(self, event):
        '''Sets up the configuration file "config.txt" to point to user defined directorys'''
        configure1 = wx.TextEntryDialog(None, "Enter the path where you want to save files", "Configure", "include the last / on *nix systems")
        if configure1.ShowModal()==wx.ID_OK:
            path = configure1.GetValue()
            path = str(path)
            f = open('conf.txt', 'w+')
            f.write(path)
            f.write("\n")
        location = wx.TextEntryDialog(None, "What do you want to call this location?", "Location", "")
        if location.ShowModal()==wx.ID_OK:
            location = location.GetValue()
            location = str(location)
            f.write(location)
            f.write("\n")
        
        configure2 = wx.TextEntryDialog(None, "Enter the path where you want to save files", "Configure", "include the last / on *nix systems")
        if configure2.ShowModal()==wx.ID_OK:
            path = configure2.GetValue()
            path = str(path)
            f.write(path)
            f.write("\n")
        location2 = wx.TextEntryDialog(None, "What do you want to call this location?", "Location", "")
        if location2.ShowModal()==wx.ID_OK:
            location2 = location2.GetValue()
            location2 = str(location2)
            f.write(location2)
            f.write("\n")
            f.close()
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
        
    def DummyPanel(self, event):
        fileDialog = wx.DirDialog(self)
        fileDialog.ShowModal()
        Name = fileDialog.GetPath()
        print Name
        
        
        #f = open(line[0].rstrip() + fileName
        
        
        

##    print "where do you want to save the file?"
##    f = open('conf.txt', 'r')
##    lines = f.readlines()
##    
##    print "1 -- " + lines[1]
##    print "2 -- " + lines[3]
##    f.close
##
##    location = int(raw_input("--->")) #Sets the variable for the if statement below this
##
##    if location == 1:
##        location = open('conf.txt', 'r')
##        line = location.readlines()
##        f = open(line[0].rstrip() + x , 'w+') #line[0].rstrip is required here to take \n off of the EOL
##        print "Sucess"
##        print line[0]
##        f.close
##        location.close
##    if location == 2:
##        location = open('conf.txt', 'r')
##        line = location.readlines()
##        f = open(line[2].rstrip() + x , 'w+')
##        print "Sucess"
##        print line[2]
##        f.close
##        location.close
##        

if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=FileMain(parent = None, id = -1)
    frame.Show()
    app.MainLoop()


print "File Creator 1.1"
print "Enter the name of the file you want to create plus the extention"
print "Or type \"configure\" to set up your custom file location "
print "ex - 'newfile.txt' "

x = raw_input("File Name --->") #User inputs the name of file and extention
if x != 'configure': 

    print "where do you want to save the file?"
    f = open('conf.txt', 'r')
    lines = f.readlines()
    
    print "1 -- " + lines[1]
    print "2 -- " + lines[3]
    f.close

    location = int(raw_input("--->")) #Sets the variable for the if statement below this

    if location == 1:
        location = open('conf.txt', 'r')
        line = location.readlines()
        f = open(line[0].rstrip() + x , 'w+') #line[0].rstrip is required here to take \n off of the EOL
        print "Sucess"
        print line[0]
        f.close
        location.close
    if location == 2:
        location = open('conf.txt', 'r')
        line = location.readlines()
        f = open(line[2].rstrip() + x , 'w+')
        print "Sucess"
        print line[2]
        f.close
        location.close

    # I dont know what this block of code does. So im just gonna comment it in case it's important.   
    #if location == 3:
        #open the config file
        #f = open('conf.txt', 'r')
        #text = f.read()

        #open the file that the config points to
        #n = open (text, 'r')
        #print  "Sucess"

        #f.close
        #n.close
    #this is some extra code to see if things auto-sync
    
else:
    f = open('conf.txt', 'w+')
    print "Write the full path of where you want to save your file include the final forward slash on *nix"
    path = raw_input("--->")
    f.write(path)
    f.write("\n")
    name = raw_input("What do you want to call this location?")
    f.write(name)
    second = raw_input("If you want to have a second file path to use, type the path here, otherwise press enter")
    f.write("\n")
    f.write(second)
    secondName = raw_input("What do you want to call this location")
    f.write("\n")
    f.write(secondName)
    f.close
    

    
exit(0)





#/Users/colin/Desktop
