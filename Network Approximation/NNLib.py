# 11/2015 NNlib
# AAAAA

## Commented by: Aleksander Mercik Mar 2017
## ========================================
## Neural Network Library

import math #Imports
import os.path
from random import random
import pickle #this import is used for data saving


class Network: #class definition
    def __init__(self, id="DEFAULT", sizes=[1, 1, 1], bias=1): #initialize with some defaults for no user specifications
        self.ID = id #set the id of the network
        if self.ID == "DEFAULT": #if the network is a default network
            self.__createdefault(sizes, bias) #internal create network
        else: 
            if os.path.exists("data/" + self.ID + ".netdata"): #check if the network exists
                if sizes!=[1, 1, 1] or bias != 1: #error checking / warning
                    print "WARNING: This network already exists and cannot be modified during loading"
                self.load() #load the network file if it exists
            else: #if the network is new
                self.__createdefault(sizes, bias) #create a new network
                self.save() #save the network

    def save(self): #save function
        if not os.path.isdir("data"): #is there a save directory
            os.makedirs("data") #make a directory if there is no save directory
        dataWrite = open("data/" + self.ID + ".netdata", "wb") #write the save file
        pickle.dump([self.Size, self.Bias, self.Neurons], dataWrite, -1) #dump information to the save file

    def load(self): #load function
        if not os.path.exists("data/" + self.ID + ".netdata"): #is ther something to load
            print "ERROR: No data to load from"
            return
        dataRead = open("data/" + self.ID + ".netdata", "rb") #read the loaded file
        inData = pickle.load(dataRead) #read the data
        self.Size = inData[0] #set the read data
        self.Bias = inData[1]
        self.Neurons = inData[2]

    def printNet(self): #print the values inside the network(weights, sums, learning values, ect...
        for i in self.Neurons: #for every neuron
            for j in i:
                print j.Weights, ":", j.sum, j.delta, ":", self.Neurons.index(i), i.index(j) #print everything

    def __createdefault(self, sizes, bias): #create a network based on input values
        self.Size = sizes #network size ie. [1, 2, 1]
        self.Neurons = [] #empty list for neuron creation
        for i in range(len(sizes)): #create the neuron array
            self.Neurons.append([])
        self.Bias = bias #set the bias
        for i in range(len(sizes) - 1): #fill the neuron array
            for j in range(int(sizes[i])):
                W = [] #empty weight array
                for k in range(int(sizes[i + 1])):
                    W.append(random() - 0.5) #append weights for the network
                self.Neurons[i].append(Neuron(W)) #append a neuron with the created weight array to the layer
            W = [] #clear the weight list
            for k in range(int(sizes[i + 1])): #append BIAS to last element of desired layers
                W.append(random() - 0.5)
            self.Neurons[i].append(Neuron(W, sum=self.Bias, isBias=True)) #special bias creation
        for i in range(self.Size[-1]): #append output neurons
            self.Neurons[-1].append(Neuron([1]))

    def forward(self, IN, isLearn = False): #forward function: run the network
        if len(IN) != self.Size[0]: #error checking for input size
            print "ERROR: Input size invalid"
            return
        # In
        for i in range(len(self.Neurons[0])-1): #add to the inputs
            self.Neurons[0][i].add(IN[i]) #add
            outTemp = self.Neurons[0][i].forward() # run the neurons
            for j in range(len(outTemp)): # add their outputs to the next layer
                self.Neurons[1][j].add(outTemp[j])
        outTemp = self.Neurons[0][-1].forward() #first BIAS
        for j in range(len(outTemp)): #add the bias output
            self.Neurons[1][j].add(outTemp[j])
        # Hidden
        for i in range(1, len(self.Neurons)-1): #run through each hidden layer
            for j in range(len(self.Neurons[i])-1): #for every neuron in the hidden layer
                self.Neurons[i][j].sigf() #activation function
                outTemp = self.Neurons[i][j].forward() #get the output
                for k in range(len(outTemp)): #add to the next layer
                    self.Neurons[i+1][k].add(outTemp[k])
            outTemp = self.Neurons[i][-1].forward() #bias
            for k in range(len(outTemp)): #add the bias
                self.Neurons[i+1][k].add(outTemp[k])
        # Out
        out = [] #output list creation for final values
        for i in range(len(self.Neurons[-1])): #get the output of every final neuron
            self.Neurons[-1][i].sigf() #activation function
            out.append(self.Neurons[-1][i].sum) #output
        # Return
        # self.printNet()
        if not isLearn: #not learning will clear the network. if the network is learning, will use the values it just calculated
            self.__clean() #clean function
        return out #return the output values

    def backprop(self, IN, EOUT, K=0.1): #backpropgation algorithm for learning
        if len(EOUT) != self.Size[-1]: #error checking for output size
            print "ERROR: Output size invalid"
            return
        elif len(IN) != self.Size[0]: #error checking for input size
            print "ERROR: Input size invalid"
            return
        self.forward(IN, isLearn=True) #forward the input values and KEEP THE INTERNAL VALUES FOR CALCULATION
        for i in self.Neurons[-1]: #for every bias
            i.delta = i.sum*(1.0-i.sum)*(i.sum - EOUT[self.Neurons[-1].index(i)]) #conpute the learning delta
        for i in self.Neurons[-2:0:-1]: #for every layer, going backwards
            for j in i[0:-1]: #for every nueron
                tSum = 0 #temp sum
                for k in j.Weights: #for all the weights
                    tSum+=k*self.Neurons[self.Neurons.index(i)+1][j.Weights.index(k)].delta #modify based on caluclated delta
                j.delta = j.sum*(1-j.sum)*tSum #set the delta
        for i in self.Neurons[0:-1]: #add weights for non bias neurons
            for j in i:
                for k in j.Weights:
                    j.Weights[j.Weights.index(k)] += -K*j.sum*self.Neurons[self.Neurons.index(i)+1][j.Weights.index(k)].delta #add delta
        self.__clean() #clean the network for next use

    def __clean(self):
        for i in self.Neurons:
            for j in i:
                if not j.isBias:
                    j.sum = 0
                else:
                    j.sum = self.Bias

    def __sigfd(self, x):
        return self.__sigf(x) * (1 - self.__sigf(x))

    def __sigf(self, x):
        return 1.0 / (1.0 + math.exp(-x))


class Neuron:
    def __init__(self, weights, sum = 0, isBias = False):
        self.sum = sum
        self.Weights = weights
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
