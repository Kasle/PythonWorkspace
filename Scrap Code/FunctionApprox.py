from NNLib import Network as Net;
import random;
import math;

App = Net("AP_005", [1, 3, 3, 3, 1]);

for i in range(10000):
    INP = random.random();
    App.backprop([INP], [INP**2]);

#INP = random.random()*10; 
#print App.forward([INP])[0], (math.sin(INP)/2)+0.5;

for i in range(100):
    print (str(App.forward([i/100.0])[0]) + "\t" + str((i/100.0)**2));