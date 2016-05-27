import NNetwork
from PIL import Image 
from time import time
import random
import os
import math

pSize = 10
iAmount = 10
fileType = "Numbers"

Net = NNetwork.Network("AutoencoderNumbers_v10.0", [pSize ** 2, iAmount*10, pSize**2])

if not os.path.exists("IOut/"+fileType+"/" + Net.ID):
    os.makedirs("IOut/"+fileType+"/" + Net.ID);

_INPUT = []

print "Loading Images"

for j in range(1, iAmount+1):
    im = Image.open("IInput/"+fileType+"/"+str(j)+".bmp")
    _INPUT.append([(sum(i)/765.0) for i in list(im.getdata())])

print  "Starting."

tDelta = 0
K = 0.001

tests = 10000
imageEvery = 5

for i in range(1,tests+1):
    tS = time()
    r = random.randint(0, len(_INPUT)-1)
    _timeSeconds = ((tests-i)*tDelta)
    _timeHours = int(_timeSeconds / 3600.0)
    _timeSeconds = _timeSeconds - (_timeHours * 3600)
    _timeMinutes = int(_timeSeconds / 60.0)
    _timeSeconds = int(_timeSeconds - (_timeMinutes * 60))
    _time = [str(_timeHours), str(_timeMinutes), str(_timeSeconds)]
    
    print 100*(i/float(tests)),"% Complete; ETA (HH:MM:SS):", ":".join(_time),"; Image:",r+1
    IMG = _INPUT[r]
    Net.backProp(IMG, IMG, K)
    if not i % imageEvery:
        tOut = []
        oPix = Net.forward(IMG)
        for j in oPix:
            val = int(255 * j)
            tOut+=[(val, val, val)]
        t = Image.new('RGB', (pSize, pSize))
        t.putdata(tOut)
        t.save("IOut/"+fileType+"/" + Net.ID + "/" + str(i)+".bmp")
    tDelta = ((tDelta * i) + (time()-tS)) / (i+1)
for i in range(iAmount):
    oPix = Net.forward(_INPUT[i])
    tOut = []
    for j in oPix:
        val = int(255 * j)
        tOut+=[(val, val, val)]
    t = Image.new('RGB', (pSize, pSize))
    t.putdata(tOut)
    t.show()