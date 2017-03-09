## Commented by: Aleksander Mercik Mar 2017
## ========================================
## Code uses a neural network to approximate NOT ( XOR ).

from NNLib import Network as Net #Import libraries
import math
import random

for j in range(50): #Test the following 50 times
    avg = [] #unused list
    for i in range(10): #Unused loop / useless
        N = Net(sizes=[2, 1, 1]) #Create a netowrk object
        count = 0 #unused count
        while True: #forever
            count += 1 #incrament the count
            inp = [random.randint(0, 1), random.randint(0, 1)] #set the input
            out = 0 #the following lines set the output
            if sum(inp) == 0 or sum(inp) == 2:
                out = 1
            N.backprop(inp, [out]) #call the network learn function. give it the input and the output
            inp = [random.randint(0, 1), random.randint(0, 1)] #get another input
            print N.forward(inp)[0] #display to the user the output.
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
