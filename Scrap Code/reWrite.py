inFile = ""

a = open(inFile, 'r')
b = a.readlines()
a.close()
a = open(inFile, 'w')
checkString = ""
for i in b:
    if checkString in i:
        spl = i.split(":")
        spl[-1] = spl[-1].split(",")
        
