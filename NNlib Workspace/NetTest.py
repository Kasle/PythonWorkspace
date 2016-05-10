from NNLib import Network as N
import random

#A = N(sizes = [1, 2, 1])
#
#for i in range(10000):
#    _IN = [random.randint(0, 1)]
#    _OUT = [1-_IN[0]]
#    A.backprop(_IN, _OUT)
#    print _IN, _OUT, A.forward(_IN)
#    
#
f = open("out.txt", 'w')
a = N(sizes=[4, 3, 1])

for i in range(5000):
    _IN = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
    _tSum = 1*_IN[0] + 2*_IN[1] + 4*_IN[2] + 8*_IN[3];
    _OUT = [1-(_tSum%2)]
    LEARN = 0.1-((i/1000000.0)**0.5)
    if (_OUT[0]==1 and i%10== 0):
        print a.forward(_IN)[0]
        f.write(str(a.forward(_IN)[0])+"\n")
    
    a.backprop(_IN, _OUT, K=0.01)
    #print _IN, a.forward(_IN)