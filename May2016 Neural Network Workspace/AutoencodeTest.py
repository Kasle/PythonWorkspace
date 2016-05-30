import NNetwork
from PIL import Image 
from time import time
import random
import os
import math

sourcePath = "IInput\\Birds\\"
imageList = [f for f in os.listdir(sourcePath) if os.path.isfile(os.path.join(sourcePath, f))]

compressedSize = 20

encodedSize = 100

imageInputList = []

print "Loading Images"

for j in imageList:
    im = Image.open(sourcePath+j).resize((compressedSize, compressedSize), Image.ANTIALIAS)
    imageInputList.append([(sum(i)/(255.0*3)) for i in list(im.getdata())])

Net = NNetwork.Network(''.join(random.choice("A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")) for _ in range(10)), shape=[len(imageInputList[0]),encodedSize,len(imageInputList[0])])

print "Original Size:",len(imageInputList[0]),"; Encoded Size", encodedSize

outputPath = "IOut\\"+''.join(random.choice("A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")) for _ in range(10))+"\\"

if not os.path.exists(outputPath):
    os.makedirs(outputPath);

print  "Starting."

tDelta = 0
K = 0.01

tests = 1000
imageEvery = 1

r=-1

for i in range(1,tests+1):
    tS = time()
    r+=1
    if r > len(imageInputList)-1:
        r = 0
    _timeSeconds = ((tests-i)*tDelta)
    _timeHours = int(_timeSeconds / 3600.0)
    _timeSeconds = _timeSeconds - (_timeHours * 3600)
    _timeMinutes = int(_timeSeconds / 60.0)
    _timeSeconds = int(_timeSeconds - (_timeMinutes * 60))
    _time = [str(_timeHours), str(_timeMinutes), str(_timeSeconds)]
    print 100*(i/float(tests)),"% Complete; ETA (HH:MM:SS):", ":".join(_time),"; Image:",r+1, ";", tDelta
    IMG = imageInputList[r]
    Net.backProp(IMG, IMG, K)
    if not i % imageEvery:
        tOut = []
#        tOut2 = []
        oPix = Net.forward(IMG)
        for j in range(len(oPix)):
            val1 = int(255 * oPix[j])
#            val2 = int(255 * IMG[j])
            tOut+=[(val1, val1, val1)]
#            tOut2+=[(val2, val2, val2)]
        t = Image.new('RGB', (compressedSize, compressedSize))
        t.putdata(tOut)
        t.save(outputPath + str(i)+"_"+str(r)+".bmp")
#        t = Image.new('RGB', (compressedSize, compressedSize))
#        t.putdata(tOut2)
#        t.save(outputPath + str(i)+"_"+str(r)+"_2.bmp")
    tDelta = ((tDelta * i) + (time()-tS)) / (i+1)
for i in imageInputList:
    tOut = []
    iN = Net.forward(i)
    for j in iN:
        val1 = int(255 * j)
        tOut+=[(val1, val1, val1)]
    t = Image.new('RGB', (compressedSize, compressedSize))
    t.putdata(tOut)
    t.save(outputPath+Net.ID+"_"+str(imageInputList.index(i))+"_"+".bmp")