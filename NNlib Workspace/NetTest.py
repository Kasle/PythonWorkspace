from NNLib import Network as N
import random

a = N(sizes=[1, 1, 1])
print a.forward([1])
a.printNet()

exit()

for i in range(5000):
    _IN = [random.randint(0, 1), random.randint(0, 1)]
    _OUT = [int((sum(_IN)==2))]
    print _IN,_OUT
    a.backprop(_IN, _OUT, K=0.01)
    print a.forward(_IN)
