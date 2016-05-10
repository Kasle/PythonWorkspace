from tables.file import openFile

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

from NNlib import Network as Net
from PressureMap import PressureMap
import random

PM = PressureMap(10, nodes = 5)
PM.roundMap()
PM.printMap()
lxy = [random.randint(0, PM.size-1),random.randint(0, PM.size-1)]
a=[]
PART = []
for i in range(PM.size):
    for j in range(PM.size):
        a.append(0)
    PART.append(a)
    a=[]

PART[lxy[0]][lxy[1]]=1

for i in PART:
    print i

for i in range(10):
    if (lxy[0]==0 or lxy[0]==PM.size-1) or (lxy[1]==0 or lxy[1]==PM.size-1):
        break
    move = [0, 0]
    cp= PM.map[lxy[0]][lxy[1]]
    ro = [PM.map[lxy[0]+1][lxy[1]], PM.map[lxy[0]][lxy[1]+1], PM.map[lxy[0]-1][lxy[1]], PM.map[lxy[0]][lxy[1]-1]]
    print ro
    break





# S2N = Net(id="SIM2\SIM2ID601", sizes=[26,26, 26,25])
#
# index = [0, 1]
#
# err = [0, 0, 0, 0, 0]
#
# while True:
#
#     err[index[0]] = errorCheck(S2N.forward(combine(pos[index[0]])), index[1])
#
#     S2N.backprop(combine(pos[index[0]]), combine(pos[index[1]]), K=sum(err)/25)
#
#     index[0]+=1
#     index[1]+=1
#     if index[0] >= 5:
#         index = [0, 1]
#     if index[1] >= 5:
#         index = [4, 0]
#
#     try:
#         S2N.save()
#     except:
#         print "ERROR: Invalid Saving. Exiting."
#         exit()

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
