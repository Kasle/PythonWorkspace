#==============================================================================
#     Math based Neural Netowrk Python Library
#     Aleks Mercik
#     May 2016
#==============================================================================

import os
import pickle
import numpy as np
import random
import math

#hadamard

class Network:
    def __init__(self, ID="DEFAULT", shape=[1,1,1], bias = 0.73):
        shape+=[0]
        self.bias = bias
        self.N = [] #Create network and weight list
        for i in range(len(shape)-1):
            self.N.append([[],[],[]])
            for j in range(shape[i]):
                self.N[-1][0].append(0)
                self.N[-1][1].append(0)
                self.N[-1][2].append((2*np.random.random([shape[i+1]]))-1)
            if i != len(shape)-2:
                self.N[-1][2].append(np.random.random([shape[i+1]]))
            self.N[i][0] = np.array(self.N[i][0])
            self.N[i][1] = np.array(self.N[i][1])
        shape.pop()
        self.__flush()

    def forward(self, networkInput):
        self.__flush()
        self.N[0][0] = np.array(networkInput)
        for i in range(len(self.N)-1):
            self.N[i][1] = np.array([self.__sigF(j) for j in self.N[i][0]])
            for j in range(len(self.N[i][1])):
                self.N[i+1][0] += self.N[i][1][j] * self.N[i][2][j]
            self.N[i+1][0]+= self.bias * self.N[i][2][-1]
        self.N[-1][1] = np.array([self.__sigF(j) for j in self.N[-1][0]])
        return list(self.N[-1][1])
    
    def __sigF(self, x):
        return 1 / (1 + math.exp(-x))
        
    def __flush(self):
        for i in range(len(self.N)):
            self.N[i][0] = np.array(np.zeros(len(self.N[i][0])))
		
Net = Network(shape=[1, 1, 1])
print Net.forward([1]),"\n"
for i in Net.N:
    for j in i:
        print j
print "\n",Net.forward([1])
#print Net.N
#print Net.N
#Net.N[-1].pop(-1)
#print 2*Net.N[-1][-1][-1]