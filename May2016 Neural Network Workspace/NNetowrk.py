#==============================================================================
#     Neural Netowrk Python Library
#     Aleks Mercik
#     May 2016
#==============================================================================

from time import time
import numpy
import math

class Network:
    def __init__(self, ID="DEFAULT", shape=[10, 10, 10], bias = 1):
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
        self.clear()
        for i in range(len(self.NodeNet[0][0:-1])):
            self.NodeNet[0][i].add(inValues[i])
        for i in self.PathNet:
            self.NodeNet[i.endIndex[0]][i.endIndex[1]].add(self.NodeNet[i.startIndex[0]][i.startIndex[1]].output()[1]*i.weight)   
        return [i.output()[1] for i in (self.NodeNet[-1])]
    
    def addPath(self, sIndex, eIndex):
        for i in range(len(self.PathNet)):
            if sIndex[0] == self.PathNet[i].startIndex[0]:
                self.PathNet.insert(i, Path(sIndex, eIndex))
                break
        

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
        
    def clear(self):
        for i in self.NodeNet:
            for j in i:
                if not j.isBias:
                    j.sum = [0, 0]
                else:
                    j.sum = [self.biasValue, 0]

class Path:
    def __init__(self, startIndex, endIndex):
        self.weight = (numpy.random.random()*2)-1
        self.startIndex = startIndex
        self.endIndex = endIndex
    def pathInfo(self):
        return str(self.startIndex) + " --" + str(self.weight) + "--> " + str(self.endIndex)

class Node:
    def __init__(self, isBias = False):
        self.sumSigged = False
        self.sum = [0, 0]       
        self.delta = 0
        self.isBias = isBias

    def sigF(self):
        try:
            self.sum[1] = 1.0 / (1.0 + math.exp(-self.sum[0]))
        except:
            pass
        
    def output(self):
        if not self.sumSigged:
            self.sigF()
            self.sumSigged = True
        return self.sum
        
    def add(self, a):
        self.sum[0]+=a
        if self.sumSigged:
            self.sumSigged = False

av=[]
ts = 0
for i in range(1):
    Net = Network(shape=[500, 500, 500, 500])
    st= time()
    out = Net.forward([1]*500)
    tt = time()-st
    ts = ((ts*i)+sum(out)/500)/float(i+1)
    av +=[tt]
print ts
print "Time:",1000*sum(av)/len(av),"ms"