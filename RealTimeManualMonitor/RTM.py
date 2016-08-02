from msvcrt import getch as get     
import customFunctions as cF
from time import time

name = raw_input("Enter output filename: ")

a = open(name+'.txt','w')

tx = 0

start = time()

while True:
    
    ts = int(time())
    while True:
        key =  ord(get())
        if time 
        if key == 27: #ESC
            a.close()
            exit()
#    te = int(time()) - ts
#    for i in range(te - 1):
#        tw = cF.addTime('00:00:00', '0:0:'+str(tx)) + ",0"
#        print tw, time()-start
#        a.write(tw+"\n")
#        tx += 1 
#    tw = cF.addTime('00:00:00', '0:0:'+str(tx)) + ",1"
#    print tw, time()-start
#    a.write(tw+"\n")
#    tx += 1 
#       