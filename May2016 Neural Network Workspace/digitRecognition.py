import NNetwork
from PIL import Image 
import os
import customFunctions as F
import time

sourcePath = "IInput\\Numbers\\"
imageList = [f for f in os.listdir(sourcePath) if os.path.isfile(os.path.join(sourcePath, f))]

imageInputList = []

print "Loading Images"

#for j in imageList:
#    im = Image.open(sourcePath+j)
#    print sourcePath+j,":"
#    print [round(k,3) for k in Net.forward([(sum(i)/(255.0)) for i in list(im.getdata())])]
#    
#exit()

for j in imageList:
    im = Image.open(sourcePath+j)
    print sourcePath+j
    imageInputList.append([(sum(i)/(255.0)) for i in list(im.getdata())])
    

#Net = NNetwork.Network(ID="DigitRec_v5", shape=[len(imageInputList[0]),25,4])
#
#print  "Starting."
#
#K = 0.01
#
#testNum = 1000
#
#for i in range(testNum):
##    ts = time.time()
#    for j in range(len(imageInputList)):
#        binReturn = F.intToBinary(j)
#        inp = F.cListToFloat((list("0"*(4-len(binReturn))+binReturn)))
#        Net.backProp(imageInputList[j], inp,K)
#        if not i%10:
#            temp = Net.forward(imageInputList[j])
#            print "OUTPUT:",inp,[round(p) for p in temp], inp==[round(p) for p in temp]
#    if not i%100:
#        Net.save()
#        print "-- OVERALL ---------------------------------------------"
#        for l in imageInputList:
#            temp = Net.forward(l)
#            print "OUTPUT:",[round(p, 3) for p in temp]
#        print "-- END OVERALL ---------------------------------------------"
##    tr = (time.time() - ts) * (testNum - i)
###    print "ETA:",tr
#
#Encode = NNetwork.Network(ID="DigitRecEncode_4.0", shape=[len(imageInputList[0]),10, 4])
#Decode = NNetwork.Network(ID="DigitRecDecode_4.0", shape=[4, 10, 10])
#
#print  "Starting."
#
#K = 0.01
#
#testNum = 100000
#
#ERRs = [[], [], [], [], [], [], [], [], [], []]
#cnt = 0
#
#for i in range(testNum):
#    for image in range(len(imageInputList)):
#        Num = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#        Num[image] = 1.0
#        EncOut = Encode.forward(imageInputList[image])
#        Decode.backProp(EncOut, Num, K)
#        DecodeInputPropagated =  [node.sum[0] for node in Decode.nodeNet[0]][0:-1]
#        Encode.backProp(imageInputList[image], DecodeInputPropagated, K)
#    if not i%100:
#        print "--",i, "--------------------------------------------------------"
#        for image in range(len(imageInputList)):
#            Num = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#            Num[image] = 1.0
#            EncOut = Encode.forward(imageInputList[image])
#            print [round(o, 3) for o in Decode.forward(EncOut)]