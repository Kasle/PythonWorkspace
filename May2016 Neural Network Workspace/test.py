import NNetwork
import random

outputs = []

#oFile = open("netOut.csv", 'w')
#for i in range(101):
#    oFile.write(","+str((i-50)/5.0))
#oFile.write("\n")
#
#for i in range(101):
#    x = (i-50)/5.0
#    oFile.write(str(x))
#    for j in range(101):
#        y = (j-50)/5.0
#        netOut = round(Net.forward([x, y])[0], 5)
#        print x, y
#        oFile.write(","+str(netOut))
#    oFile.write("\n")
#oFile.close()
#
#MS = [(i+1)*2 for i in range(10)]
#ERR = []

#for j in MS:
Net = NNetwork.Network(shape = [2,4,1])    

Err = 0

K = 2

count = 0

for i in range(100000):
    count+=1
    _in = [10*random.random() - 5, 10*random.random()-5]
    _out = [abs(sum(_in))/20]
#    if (_in[0] < 2.5 and _in[0] > -2.5) or (_in[1] > -2.5 and _in[1] < 2.5):
#        _out = [1]
    Net.backProp(_in, _out, K)
#    nOut = Net.forward(_in)[0]
#    Err += abs(nOut - _out[0])
#print j, Err
        
oFile = open("netOut.csv", 'w')
for i in range(101):
    oFile.write(","+str((i-50)/5.0))
oFile.write("\n")

for i in range(101):
    x = (i-50)/5.0
    oFile.write(str(x))
    for j in range(101):
        y = (j-50)/5.0
        netOut = round(Net.forward([x, y])[0], 5)
        print x, y
        oFile.write(","+str(netOut))
    oFile.write("\n")
oFile.close()