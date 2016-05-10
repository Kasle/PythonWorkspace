import random
import math

class PressureMap:
    def __init__(self, size, nodes=1, decay=0.5, nodemag = 1):
        self.size = size
        self.nnodes = nodes
        self.decay = decay
        self.map = self.setMap()
        self.nodemag = nodemag
        for i in range(self.nnodes):
            self.applyNewNode()

    def applyNewNode(self):
        nxy = [random.randint(0, self.size-1), random.randint(0, self.size-1)]
        nmag = 1*self.nodemag
        for i in range(self.size):
            for j in range(self.size):
                decayscale = math.pow(self.decay, math.sqrt(math.pow(nxy[0]-i, 2)+math.pow(nxy[1]-j, 2)))
                self.map[i][j]+=decayscale*nmag

    def setMap(self):
        a = []
        b = []
        for i in range(self.size):
            for j in range(self.size):
                a.append(0)
            b.append(a)
            a=[]
        return b

    def setRandomMap(self):
        for i in range(self.size):
            for j in range(self.size):
                self.map[i][j] = random.random()

    def roundMap(self):
        for i in range(self.size):
            for j in range(self.size):
                self.map[i][j] = round(self.map[i][j], 2)

    def printMap(self):
        for i in self.map:
            print i