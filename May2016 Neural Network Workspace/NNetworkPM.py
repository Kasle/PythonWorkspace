#==============================================================================
#     Pure Math based Neural Netowrk Python Library
#     Aleks Mercik
#     May 2016
#==============================================================================

import os
import pickle
import numpy
import random
import math

class Network:
    def __init__(self, ID="DEFAULT", shape=[1,1,1], bias = 1):
        shape+=[0]
        self.N = [[[bias,[1]*shape[i+1]]]*(shape[i]+1) for i in range(len(shape)-1)] #Create network and weights
        self.__flush()
    
    def __sigF(self, x):
        return 1 / (1 + math.exp(-x))
        
    def __flush(self):
        
		

		
Net = Network(shape=[1,3,1])
print Net.N