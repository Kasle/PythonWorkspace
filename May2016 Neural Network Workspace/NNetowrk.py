#==============================================================================
#     Neural Netowrk Python Library
#     Aleks Mercik
#     May 2016
#==============================================================================

from time import time
from time import sleep
import random
import numpy
import math

class NNetwork:
    def __init__(self, ID="DEFAULT", shape=[10, 50, 10], bias = 1):
        self.NodeNet = []
        self.PathNet = []
        self.ID = ID
        self.shape = shape
        self.biasValue = bias
#        if self.ID == "DEFAULT":
#            print "Creating temporary network."
#        else:
#            print "Creating and saving network " + self.ID + "."
        self.makeNet()
            
    def save(self):
        print "Saving network " + self.ID + "."
        
    def load(self):
        print "Loading newtork " + self.ID + "." 
        
    def forward(self, inValues):
        for i in range(len(self.NodeNet[0][0:-1])):
            self.NodeNet[0][i].add(inValues[i])
        for i in self.PathNet:
            self.NodeNet[i.endIndex[0]][i.endIndex[1]].add(self.NodeNet[i.startIndex[0]][i.startIndex[1]].outSigF()[1]*i.weight)
        
        return [i.outSigF()[1] for i in (self.NodeNet[-1])]

    def makeNet(self):
        for i in self.shape:
            tempLayer = [Node() for j in range(i+1)]
            tempLayer[-1].isBias = True
            tempLayer[-1].sum[0] = 3
            self.NodeNet.append(tempLayer)
        
        for i in range(len(self.NodeNet)-1):
            for j in range(len(self.NodeNet[i])):
                for k in range(len(self.NodeNet[i+1])-1):
                    self.PathNet.append(Path([i,j],[i+1,k]))
        self.NodeNet[-1].pop()

class Path:
    def __init__(self, startIndex, endIndex):
        self.weight = (numpy.random.random()*2)-1
        self.startIndex = startIndex
        self.endIndex = endIndex
        #print self.startIndex,"--",self.weight,"-->",self.endIndex

class Node:
    def __init__(self, isBias = False):
        self.sum = [0, 0]       
        self.delta = 0
        self.isBias = isBias

    def outSigF(self):
        try:
            self.sum[1] = 1.0 / (1.0 + math.exp(-self.sum[0]))
        except:
            pass
        return self.sum

    def add(self, a):
        self.sum[0]+=a

av=0
ts = 0
for i in range(1000):
    st= time()
    Net = NNetwork(shape=[10, 100, 100, 10])
    ts = ((ts*i)+sum(Net.forward([1,1, 1, 1, 1, 1, 1, 1, 1, 1]))/10.0)/(i+1)
    tt = time()-st
    av = ((av*i)+tt)/float(i+1)
print ts
print av