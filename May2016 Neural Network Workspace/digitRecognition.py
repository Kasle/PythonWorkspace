import NNetwork
from PIL import Image 
from time import time
import random
import os
import math

sourcePath = "IInput\\Numbers\\"
imageList = [f for f in os.listdir(sourcePath) if os.path.isfile(os.path.join(sourcePath, f))]

rootZoneSize = 50

imageInputList = []

print "Loading Images"

for j in imageList:
    im = Image.open(sourcePath+j)
    imageInputList.append([(sum(i)/(255.0*3)) for i in list(im.getdata())])

Net = NNetwork.Network(ID="DigitRec_v7.0", shape=[len(imageInputList[0]),rootZoneSize*2,10])

print  "Starting."

tDelta = 0
K = 0.01

tests = 10000

r=-1

ERROR=0

for i in range(1,tests+1):
    tS = time()
    r+=1
    if r > len(imageInputList)-1:
        r = 0
    _timeSeconds = ((tests-i)*tDelta)+1
    _timeHours = int(_timeSeconds / 3600.0)
    _timeSeconds = _timeSeconds - (_timeHours * 3600)
    _timeMinutes = int(_timeSeconds / 60.0)
    _timeSeconds = int(_timeSeconds - (_timeMinutes * 60))
    _time = [str(_timeHours), str(_timeMinutes), str(_timeSeconds)]
    IMG = imageInputList[r]
    OUT = [round(j, 3) for j in Net.forward(IMG)]
    print 100*(i/float(tests)),"% Complete; ETA (HH:MM:SS):", ":".join(_time),"; Number:",r, ";", ERROR,";",OUT
    ERROR = 0
    outputList = [-10, -10, -10, -10, -10 , -10, -10, -10, -10, -10]
    outputList[r]=10
    Net.backProp(IMG, outputList, K)
    OUT = Net.forward(IMG)
    for i in range(len(OUT)):
       ERROR += abs(OUT[i] - outputList[i])
    if not i%100:
        Net.save()
    tDelta = ((tDelta * i) + (time()-tS)) / (i+1)
