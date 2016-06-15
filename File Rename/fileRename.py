import customFunctions as F
import os

_files = F.getFilesInFolder("INPUT")
print "Found Files:"
print _files
print ""

blacklist = [" ", ""]

while True:
        FNAME = raw_input("Enter Camera Code: ")
        NNAME = raw_input("Enter ID: ")
        if FNAME == "" or NNAME == "":
                print "No characters detected. Exiting."
                break
        if FNAME in blacklist or NNAME in blacklist:
                print "Blacklisted Character Detected. Please try again."
                continue
        count = 0
        for i in _files:
                if FNAME in i:
                        c = i.split(".")
                        if count == 0:
                                print "Renaming",i,"to","INPUT\\"+NNAME+"-Background."+c[-1]
                                os.rename(i, "INPUT\\"+NNAME+"-Background."+c[-1])
                        else:
                                print "Renaming",i,"to","INPUT\\"+NNAME+"-"+str(count)+"."+c[-1]
                                os.rename(i, "INPUT\\"+NNAME+"-"+str(count)+"."+c[-1])
                        count+=1
