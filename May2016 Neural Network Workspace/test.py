import NNetwork
import random

Net = NNetwork.Network(shape=[10] + [500]*10 + [10])
print "Forwarding"
print Net.forward([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
