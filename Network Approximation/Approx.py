from NNLib import Network as Net;
import math;
import random;

for j in range(50):
    avg = []
    for i in range(10):
        N = Net(sizes=[2, 1, 1]);
        count = 0
        while True:
            count += 1
            inp = [random.randint(0, 1), random.randint(0, 1)]
            out = 0
            if sum(inp) == 0 or sum(inp) == 2:
                out = 1
            N.backprop(inp, [out])
            inp = [random.randint(0, 1), random.randint(0, 1)]
            print N.forward(inp)[0]
#count = 0;
#while True:
#    count+=1;
#    R = [random.random(), random.random()];
#    OUT = 0;
#    if (R[0] > R[1]):
#        OUT = 1;
#    K=math.exp(-(count/1000000.0))/10.0;
#    N.backprop(R, [OUT], K=K);
#    ERR = N.forward(R)[0];
#    OUT2 = 0;
#    if (R[0] > R[1]):
#        ERR = (1-ERR)
#    if (ERR < 0.001):
#        ERR = 0;
#    print "ERROR:", str(ERR)[:5] + "\t" + str(K)[:6]
#    try:    
#        N.save()
#    except:
#        print "SAVE ERROR"
