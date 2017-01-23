import os
import random

#List Functions -------------------------------------------------------------

def cListToFloat(sL):
    return [float(i) for i in sL]
    
def cListToString(sL):
    return [str(i) for i in sL]
    
def cListToInt(sL):
    return [int(i) for i in sL]

def sort(iList):
    temp = iList
    size = 1
    while 1:
        temp2 = []
        for i in range(0, len(temp), size*2):
            A = temp[i:i+size]
            B = temp[i+size:i+2*size]
            while A and B:
                if A[0] < B[0]:
                    temp2.append(A.pop(0))
                else:
                    temp2.append(B.pop(0))
            temp2 += A + B
        temp = temp2
        size*=2
        if size > len(temp):
            break
    return temp

from time import time
start = time()
for i in range(10000):
    tl = [random.randint(-100, 100) for i in range(random.randint(3, 50))]
    tl.sort()
print time() - start
    
#Matrix Operations ------------------------------------------------------------
    
def mxAdd(a, b):
    if len(a) == len(b):
        try:
            rMatrix = [a[i]+b[i] for i in range(len(a))]
            return rMatrix
        except:
            print "ERROR: Operation Failure"
            pass
    else:
        print "ERROR: Matrices are not of equal length"
    return None
    
def mxSubtract(a, b):
    if len(a) == len(b):
        try:
            rMatrix = [a[i]-b[i] for i in range(len(a))]
            return rMatrix
        except:
            print "ERROR: Operation Failure"
            pass
    else:
        print "ERROR: Matrices are not of equal length"
    return None
    
def mxDivide(a, b):
    if len(a) == len(b):
        try:
            rMatrix = [a[i] / float(b[i]) for i in range(len(a))]
            return rMatrix
        except:
            print "ERROR: Operation Failure"
            pass
    else:
        print "ERROR: Matrices are not of equal length"
    return None
        
def mxMultiply(a, b): #Hadamard
    if len(a) == len(b):
        try:
            rMatrix = [a[i]*b[i] for i in range(len(a))]
            return rMatrix
        except:
            print "ERROR: Operation Failure"
            pass
    else:
        print "ERROR: Matrices are not of equal length"
    return None

#Number Operations ------------------------------------------------------------

def splitDecimal(nIn): # Takes a number, splits it at the decimal, then returns the decimal and the number.
    rList= (str(float(nIn)).split("."))
    rList[1] = "0."+rList[1]
    return cListToFloat(rList)
    
def rangeMap(value, valLow, valHigh, numLow, numHigh, constrain = False):
    valDiff = abs(valHigh-valLow)
    numDiff = abs(numHigh-numLow)
    temp = value
    if temp > valHigh and constrain: temp = valHigh
    elif temp < valLow and constrain: temp = valLow 
    temp =  (((temp - valLow) / float(valDiff)) * numDiff)+numLow
    return temp
    
def intToBinary(inp):
    try:
        outStr = ""
        temp = inp
        curr = 2
        processed = 0
        if temp == 0:
            return "0"
        while True:
            if (temp-processed) % curr:
                outStr="1"+outStr
                processed += curr / 2
            else:
                outStr="0"+outStr
            if curr > temp:
                break
            curr*=2
        return outStr
    except:
        return "0"

#Time Operations --------------------------------------------------------------

def addTime(tStart, tAdd): # Eg. ("11:25:03", "00:01:05"), ("HH:MM:SS","HH:MM:SS" to add)
    cTime = cListToFloat(tStart.split(":"))
    aTime = cListToFloat(tAdd.split(":"))
    tTime = mxAdd(cTime, aTime)
    if tTime[2] >= 60:
        temp = splitDecimal(tTime[2] / 60.0)
        tTime[2]=temp[1]*60
        tTime[1]+=temp[0]
    if tTime[1] >= 60:
        temp = splitDecimal(tTime[1] / 60.0)
        tTime[1]=temp[1]*60
        tTime[0]+=temp[0]
    if tTime[0] >= 24:
        temp = splitDecimal(tTime[0] / 24.0)
        tTime[0] = temp[1] * 24
    tTime[0] = int(round(tTime[0]))
    if len(str(tTime[0])) == 1:
        tTime[0] = "0"+str(tTime[0])
    tTime[1] = int(round(tTime[1]))
    if len(str(tTime[1])) == 1:
        tTime[1] = "0"+str(tTime[1])
    tTime[2] = round(tTime[2],1)
    if len(str(int(tTime[2]))) == 1:
        tTime[2] = "0"+str(tTime[2])
    return ":".join(cListToString(tTime))
    

def timeToCode(spl): # Eg. [2000, 12, 03, 23, 13, 04], [YYYY, MM, DD, HH, mm, SS]
    newValue = 38064000*float(spl[0])+2928000*float(spl[1])+91500*float(spl[2])+3660*float(spl[3])+60*float(spl[4])+float(spl[5])
    return newValue
    
#Folder Operations ------------------------------------------------------------

def getFilesInFolder(path=".", mode = 0):
    returnFiles = []
    if mode == 0:
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path, i)):
                returnFiles.append(os.path.join(path, i))
    elif mode == 1:
        for root, dirs, files in os.walk("."):
            for i in files:
                returnFiles+= [root+"\\"+i]
    return returnFiles
    
#String Functions -------------------------------------------------------------
    
def genRandomString(n):
    alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    retSt =''
    for i in range(n):
        ul = random.randint(0, 1)
        choose = alph[random.randint(0, len(alph)-1)]
        if ul:
            retSt += choose
        else:
            retSt += choose.lower()
    return retSt

#File Operations --------------------------------------------------------------

def graph(fileName, index, multiplier):
    f = open(fileName, 'r')
    rl = f.readlines()
    col = int(index)
    mult = float(multiplier)
    for i in rl[2:]:
        print int(float(i.split(",")[col]) * mult)*"#"
        
#OS Operations ----------------------------------------------------------------

from msvcrt import getch as get     
def readKeys():
    while True:
        key =  ord(get())
        print key
        if key == 27: #ESC
            break
