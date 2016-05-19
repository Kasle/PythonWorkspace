import NNetwork
import random

outputs = []

Net = NNetwork.Network(shape = [5, 6,3, 1])

for i in range(100000):
    Net.backProp([0,0,0,0,0], [0], 0.5)
    Net.backProp([1,0,0,0,0], [1], 0.5)
    Net.backProp([0,0,0,0,0], [0], 0.5)
    Net.backProp([0,1,0,0,0], [1], 0.5)
    Net.backProp([0,0,0,0,0], [0], 0.5)
    Net.backProp([0,0,1,0,0], [1], 0.5)
    Net.backProp([0,0,0,0,0], [0], 0.5)
    Net.backProp([0,0,0,1,0], [1], 0.5)
    Net.backProp([0,0,0,0,0], [0], 0.5)
    Net.backProp([0,0,0,0,1], [1], 0.5)
    
print Net.forward([0,0,0,0,0])
print Net.forward([1,0,0,0,0])
print Net.forward([0,1,0,0,0])
print Net.forward([0,0,1,0,0])
print Net.forward([0,0,0,1,0])
print Net.forward([0,0,0,0,1])