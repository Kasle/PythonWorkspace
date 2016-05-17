#==============================================================================
#     Neural Netowrk Python Library
#     Aleks Mercik
#     May 2016
#==============================================================================

from time import time
import numpy
import math

class Network:
    def __init__(self, ID="DEFAULT", shape=[1,1,1], bias = 1):
        self.nodeNet = []
        self.pathNet = []
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
        for i in range(len(self.nodeNet[0][0:-1])):
            self.nodeNet[0][i].add(inValues[i])
        for i in self.pathNet:
            for j in i:
                for k in j:
                    self.nodeNet[k.endIndex[0]][k.endIndex[1]].add(self.nodeNet[k.startIndex[0]][k.startIndex[1]].output()[1]*k.weight)   
        return [i.output()[1] for i in (self.nodeNet[-1])]
    
    def addPath(self, sIndex, eIndex):
        self.pathNet[sIndex[0]][sIndex[1]].append(Path(sIndex, eIndex))

    def makeNet(self):
        for i in self.shape:
            tempLayer = [Node() for j in range(i+1)]
            tempLayer[-1].isBias = True
            tempLayer[-1].sum[0] = 3
            self.nodeNet.append(tempLayer)
        
        for i in range(len(self.nodeNet)-1):
            self.pathNet.append([])
            for j in range(len(self.nodeNet[i])):
                self.pathNet[i].append([])
                for k in range(len(self.nodeNet[i+1])-1): # i = Path Layer, j = Node Number, k = Path
                    self.pathNet[i][j].append(Path([i,j],[i+1,k]))
        self.nodeNet[-1].pop()
        
    def clear(self):
        for i in self.nodeNet:
            for j in i:
                if not j.isBias:
                    j.sum = [0, 0]
                else:
                    j.sum = [self.biasValue, 0]

    def backProp(self, expectedInput, expectedOutput, A=1):
        self.forward(expectedInput)

        for paths in self.pathNet[-1]:
            for i in paths:
                endNodeIndex = i.endIndex
                startNodeIndex = i.startIndex
                endNodeSum = self.nodeNet[endNodeIndex[0]][endNodeIndex[1]].sum
                startNodeSum = self.nodeNet[startNodeIndex[0]][startNodeIndex[1]].sum
                i.delta = -(expectedOutput[endNodeIndex[1]] - endNodeSum[1])*endNodeSum[1]*(1-endNodeSum[1])
                i.weight -= A * i.delta * startNodeSum[1]
        
        for x in self.pathNet[0:-1]:
            for y in x:
                for i in y:
                    endNodeIndex = i.endIndex
                    startNodeIndex = i.startIndex
                    endNodeSum = self.nodeNet[endNodeIndex[0]][endNodeIndex[1]].sum
                    startNodeSum = self.nodeNet[startNodeIndex[0]][startNodeIndex[1]].sum
                    deltaSum = 0
                    for path in self.pathNet[endNodeIndex[0]][endNodeIndex[1]]:
                        deltaSum += path.delta * path.weight
                    i.delta = deltaSum*endNodeSum[1]*(1-endNodeSum[1])
                    i.weight -= A * i.delta * startNodeSum[1]
        

    def printNet(self):
        for i in self.nodeNet:
            for j in i:
                print [self.nodeNet.index(i),i.index(j)],j.sum
        for i in self.pathNet:
            for j in i:
                for k in j:
                    print k.pathInfo()

class Path:
    def __init__(self, startIndex, endIndex):
        self.weight = (numpy.random.random()*2)-1
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.delta = 0
    def pathInfo(self):
        return str(self.startIndex) + " -- " + str(self.weight) + " --> " + str(self.endIndex)

class Node:
    def __init__(self, isBias = False):
        self.sumSigged = False
        self.sum = [0, 0]       
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

##Example Of Use

##Net = Network(shape=[1, 3, 1])
##
##print Net.forward([1])
##print Net.forward([0]),"\n"
##
##for i in range(10000):
##    Net.backProp([1],[0],3)
##    Net.backProp([0],[1],3)
##
##print Net.forward([1])
##print Net.forward([0])
