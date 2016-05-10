import os

fileLoactions = []
driveX= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n" , "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def findFiles(path, fileID):
    for i in os.listdir(path):
        try:
            if os.path.isdir(path + "\\" + i) == True:
                if i.lower().find(fileID) != -1:
                    fileLocations.append(path + "\\" + i)
                findFiles(path + "\\" + i, fileID)
            elif i.lower().find(fileID) != -1:
                fileLocations.append(path + "\\" + i)
        except WindowsError:
            print "PATH :: " + path + "\\" + i + " :: DENIED"
        except:
            print "UNKNOWN ERROR :: ?? ::"
            
while True:
    fType = raw_input("Enter a file name (may be part of name) or type:")
    if fType == "**":
        break
    fileLocations = []
    print "------------------------------------------------------------"
    for i in driveX:
        try:
            findFiles(i.upper() + ":\\", fType.lower())
        except WindowsError:
            print "DRIVE :: " + i.upper() + " :: DOES NOT EXIST"
    for i in fileLocations:
        print i
    print "TOTAL FILES :: " + str(len(fileLocations))
    print "------------------------------------------------------------"
    
exit()
