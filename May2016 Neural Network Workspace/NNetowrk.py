#==============================================================================
#     Neural Netowrk Python Library
#     Aleks Mercik
#     May 2016
#==============================================================================

import random
import numpy
import math

class NNetwork:
    def __init__(self, ID="DEFAULT", shape=[1, 1, 1], bias = 1):
        self.ID = ID
        self.shape = shape
        self.biasValue = bias
        if ID == "DEFAULT":
            print "Creating temporary network."
        else:
            print "Creating and saving network " + ID + "."
            
    def save(self):
        print "Saving network " + self.ID + "."
        
    def load(self):
        print "Loading newtork " + self.ID + "." 
        

class Neuron:
    def __init__(self, Network, nextLayerSize, isBias = False):
        self.sum = 0
        self.parent = Network        
        self.weights = numpy.random.rand(nextLayerSize, 1)           
        self.delta = 0
        self.isBias = isBias

    def forward(self):
        self.output = []
        for i in range(len(self.Weights)):
            self.output.append(self.Weights[i] * self.sum)
        return self.output

    def sigf(self):
        try:
            self.sum = 1.0 / (1.0 + math.exp(-self.sum))
        except:
            self.sum = 0

    def add(self, a):
        self.sum += a