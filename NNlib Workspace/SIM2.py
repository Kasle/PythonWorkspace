from tables.file import openFile

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

from NNlib import Network as Net
import random
import time
import datetime
import os.path
import math

def printPos(inp):
    for i in inp:
        a = ""
        for j in i:
            a+=str(j)
        print a

def combine(inp):
    out = []
    for i in inp:
        out+=i
    return out

def seperate(inp, square):
    out = []
    temp=[]
    tot = 0
    while tot < len(inp):
        for i in range(square):
            temp.append(inp[i+tot])
        out.append(temp)
        temp = []
        tot+=square
    return out

pos = [
    [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
    ],
]

test = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

def errorCheck(inp, nextIndex):
    check = combine(pos[nextIndex])
    out = 0
    for i in range(len(check)):
        if check[i] == 1:
            out+= (1 - inp[i])
        elif check[i] == 0:
            out+= inp[i]
    return out

#exit()

S2N = Net(id="SIM2\SIM2ID601", sizes=[26,26, 26,25])

index = [0, 1]

err = [0, 0, 0, 0, 0]

while True:

    err[index[0]] = errorCheck(S2N.forward(combine(pos[index[0]])), index[1])

    S2N.backprop(combine(pos[index[0]]), combine(pos[index[1]]), K=sum(err)/25)

    index[0]+=1
    index[1]+=1
    if index[0] >= 5:
        index = [0, 1]
    if index[1] >= 5:
        index = [4, 0]

    try:
        S2N.save()
    except:
        print "ERROR: Invalid Saving. Exiting."
        exit()

    if sum(err) < (0.1*len(err)):
        break

    print "SUCCESS:", err


print ""
out = S2N.forward(combine(pos[4]))
temp = []
for i in out:
    temp.append(int(round(i)))

printPos(seperate(temp, 5))
print ""
out = S2N.forward(combine(pos[0]))
temp = []
for i in out:
    temp.append(int(round(i)))

printPos(seperate(temp, 5))
print ""

out = S2N.forward(combine(pos[1]))
temp = []
for i in out:
    temp.append(int(round(i)))

printPos(seperate(temp, 5))
print ""
out = S2N.forward(combine(pos[2]))
temp = []
for i in out:
    temp.append(int(round(i)))

printPos(seperate(temp, 5))
print ""
out = S2N.forward(combine(pos[3]))
temp = []
for i in out:
    temp.append(int(round(i)))

printPos(seperate(temp, 5))

print ""
out = S2N.forward(combine(test))
temp = []
for i in out:
    temp.append(int(round(i)))

printPos(seperate(temp, 5))


# #for i in range(100000):
# while True:
#     if count%1000 == 0:
#         try:
#             B.save()
#         except:
#             print "WARNING: Unstable save. Ending Safely"
#             exit()
#     if count%100000 == 0:
#         print B.forward([1, 1, 1])
#         print B.forward([0, 1, 1])
#         print B.forward([0, 0, 1])
#         print B.forward([0, 0, 0])
#     count+=1
#     a = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
#     if sum(a) == 3 or sum(a)==0:
#         out = 1
#     else:
#         out = 0
#     err1 = 1-B.forward([1, 1, 1])[0]
#     B.backprop(a, [out], K=0.01)
#
# print B.forward([1, 1, 1])
# print B.forward([0, 1, 1])
# print B.forward([0, 0, 1])
# print B.forward([0, 0, 0])
#
# # for i in range(100000):
# #     if i % 1000 == 0:
# #         print str(1-B.forward([0.6])[0] + B.forward([0.4])[0])
# #     v = random.random()
# #     if v > 0.5:
# #         out = 1
# #     else:
# #         out = 0
# #
# #     B.backprop([v], [out], K=0.01)
# #     B.save()
# # B.save()
