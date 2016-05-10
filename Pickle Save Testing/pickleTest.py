import pickle

class Net:
    def __init__(self, A):
        self.B = A

    def getB(self):
        return self.B

T = Net("B")

dataWrite = open("B.netdata", "wb")

pickle.dump(T, dataWrite, -1)

dataWrite.close()

dataRead = open("B.netdata", "rb")

nT = pickle.load(dataRead)

print nT.getB()