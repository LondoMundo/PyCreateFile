#CUSTOM FILEPATH IS BROKEN FIGURE OUT WHY f.write(str) ISNT WRITING TO conf.txt

# FILE CREATOR 1.0
# WRITTEN BY COLIN MURPHY
# THIS CODE MAY BE REDISTRIBUTED OR ALTERED, BUT NOT SOLD

#TODO

# DONE. ADD A CONFIGURATION FILE SO THE USER CAN SET WHERE FILES ARE TO BE SAVED TO
#THIS WILL MAKE THE SCRIPT WORK ON ANY COMPUTER SO LONG AS THE USER INPUTS
#THE CORRECT FILE PATHS

# 1. ALLOW FOR CUSTOMIZATION OF LINES 11-12 (WHERE THE DIALOUGE SAYS IT WILL
#SAVE THE FILE

# 2. GUI GUI GUI9
import wx
import os

class FileMain(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "File Creator", size=(500,300))
        panel = wx.Panel(self)
        configureButton = wx.Button(panel, label = "configure", pos = (200, 0), size = (125,75))
        self.Bind(wx.EVT_BUTTON, self.Configure, configureButton)


    def Configure(self, event):

        configure2 = wx.TextEntryDialog(None, "Enter the path where you want to save files", "Configure", "include the last / on *nix systems")
        if configure2.ShowModal()==wx.ID_OK:
            path = configure2.GetValue()
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
        
##        
##        print "Write the full path of where you want to save your file include the final forward slash on *nix"
##        path = raw_input("--->")
##        
##        
##        name = raw_input("What do you want to call this location?")
##        f.write(name)
##        second = raw_input("If you want to have a second file path to use, type the path here, otherwise press enter")
##        f.write("\n")
##        f.write(second)
##        secondName = raw_input("What do you want to call this location")
##        f.write("\n")
##        f.write(secondName)
##        f.close
        

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
