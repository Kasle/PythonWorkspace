# 11/2015 NNlib
# AAAAA

import math
import os.path
from random import random
import pickle
from time import time


class Network:
    def __init__(self, id="DEFAULT", sizes=[1, 1, 1], bias=1):
        self.ID = id
        if self.ID == "DEFAULT":
            self.__createdefault(sizes, bias)
        else:
            if os.path.exists("data/" + self.ID + ".netdata"):
                if sizes!=[1, 1, 1] or bias != 1:
                    print "WARNING: This network already exists and cannot be modified during loading"
                self.load()
            else:
                self.__createdefault(sizes, bias)
                self.save()

    def save(self):
        if not os.path.isdir("data"):
            os.makedirs("data")
        dataWrite = open("data/" + self.ID + ".netdata", "wb")
        pickle.dump([self.Size, self.Bias, self.Neurons], dataWrite, -1)

    def load(self):
        if not os.path.exists("data/" + self.ID + ".netdata"):
            print "ERROR: No data to load from"
            return
        dataRead = open("data/" + self.ID + ".netdata", "rb")
        inData = pickle.load(dataRead)
        self.Size = inData[0]
        self.Bias = inData[1]
        self.Neurons = inData[2]

    def printNet(self):
        for i in self.Neurons:
            for j in i:
                print j.Weights, ":", j.sum, j.delta, ":", self.Neurons.index(i), i.index(j)

    def __createdefault(self, sizes, bias):
        self.Size = sizes
        self.Neurons = []
        for i in range(len(sizes)):
            self.Neurons.append([])
        self.Bias = bias
        for i in range(len(sizes) - 1):
            for j in range(int(sizes[i])):
                W = []
                for k in range(int(sizes[i + 1])):
                    W.append(random() - 0.5)
                self.Neurons[i].append(Neuron(W))
            W = []
            for k in range(int(sizes[i + 1])):
                W.append(random() - 0.5)
            self.Neurons[i].append(Neuron(W, sum=self.Bias, isBias=True))
        for i in range(self.Size[-1]):
            self.Neurons[-1].append(Neuron([1]))

    def forward(self, IN, isLearn = False):
        if len(IN) != self.Size[0]:
            print "ERROR: Input size invalid"
            return
        # In
        for i in range(len(self.Neurons[0])-1):
            self.Neurons[0][i].add(IN[i])
            outTemp = self.Neurons[0][i].forward()
            for j in range(len(outTemp)):
                self.Neurons[1][j].add(outTemp[j])
        outTemp = self.Neurons[0][-1].forward()
        for j in range(len(outTemp)):
            self.Neurons[1][j].add(outTemp[j])
        # Hidden
        for i in range(1, len(self.Neurons)-1):
            for j in range(len(self.Neurons[i])-1):
                self.Neurons[i][j].sigf()
                outTemp = self.Neurons[i][j].forward()
                for k in range(len(outTemp)):
                    self.Neurons[i+1][k].add(outTemp[k])
            outTemp = self.Neurons[i][-1].forward()
            for k in range(len(outTemp)):
                self.Neurons[i+1][k].add(outTemp[k])
        # Out
        out = []
        for i in range(len(self.Neurons[-1])):
            self.Neurons[-1][i].sigf()
            out.append(self.Neurons[-1][i].sum)
        # Return
        # self.printNet()
        if not isLearn:
            self.__clean()
        return out

    def backprop(self, IN, EOUT, K=0.1):
        if len(EOUT) != self.Size[-1]:
            print "ERROR: Output size invalid"
            return
        elif len(IN) != self.Size[0]:
            print "ERROR: Input size invalid"
            return
        self.forward(IN, isLearn=True)
        for i in self.Neurons[-1]:
            i.delta = i.sum*(1.0-i.sum)*(i.sum - EOUT[self.Neurons[-1].index(i)])
        for i in self.Neurons[-2:0:-1]:
            for j in i[0:-1]:
                tSum = 0
                for k in j.Weights:
                    tSum+=k*self.Neurons[self.Neurons.index(i)+1][j.Weights.index(k)].delta
                j.delta = j.sum*(1-j.sum)*tSum
        for i in self.Neurons[0:-1]:
            for j in i:
                for k in j.Weights:
                    j.Weights[j.Weights.index(k)] += -K*j.sum*self.Neurons[self.Neurons.index(i)+1][j.Weights.index(k)].delta
        self.__clean()

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

av=[]
ts = 0
for i in range(1):
    Net = Network(sizes=[500, 500, 500, 500])
    st= time()
    out = Net.forward([1]*500)
    tt = time()-st
    ts = ((ts*i)+sum(out)/500.0)/float(i+1)
    av +=[tt]
print ts
print "Time:",1000*sum(av)/len(av),"ms"