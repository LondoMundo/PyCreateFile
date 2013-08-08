#CUSTOM FILEPATH IS BROKEN FIGURE OUT WHY f.write(str) ISNT WRITING TO conf.txt

# FILE CREATOR 1.0
# WRITTEN BY COLIN MURPHY
# THIS CODE MAY BE REDISTRIBUTED OR ALTERED, BUT NOT SOLD

#TODO

# DONE. ADD A CONFIGURATION FILE SO THE USER CAN SET WHERE FILES ARE TO BE SAVED TO
#THIS WILL MAKE THE SCRIPT WORK ON ANY COMPUTER SO LONG AS THE USER INPUTS
#THE CORRECT FILE PATHS

# 1. ALLOW FOR CUSTOMIZATION OF LINES 11-12 (WHERE THE DIALOUGE SAYS IT WILL
#SAVE THE FILE)

# 2. GUI GUI GUI

import os

print "File Creator 1.1"
print "Enter the name of the file you want to create plus the extention"
print "Or type \"configure\" to set up your custom file location "
print "ex - 'newfile.txt' "

x = raw_input("File Name --->") #User inputs the name of file and extention
if x != 'conf': 

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
        f = open(line[0] + x , 'w+')
        print "Sucess"
        print line[0]
        f.close
        location.close
    if location == 2:
        location = open('conf.txt', 'r')
        line = location.readlines()
        f = open(line[2] + x , 'w+')
        print "Sucess"
        print line[0]
        f.close
        location.close
    if location == 3:
        #open the config file
        f = open('conf.txt', 'r')
        text = f.read()

        #open the file that the config points to
        n = open (text, 'r')
        print  "Sucess"

        f.close
        n.close
    
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
