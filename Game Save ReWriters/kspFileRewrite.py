import os

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
            
fileLocations = []

findFiles(os.getcwd(), ".cfg")

for a in fileLocations:
    _file = open(a, "r")
    _data = _file.readlines()
    for i in range(len(_data)):
        if _data[i].find("xmitDataScalar") != -1:
            _data[i] = _data[i][:_data[i].find("=")+2] + "1.0" + "\n"
    _file.close()
    
    _file = open(a, "w")
    for i in _data:
        _file.write(i)
    _file.close()
