from tables.file import openFile

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

from NNlib import Network as Net
import random
import time
import datetime
import os.path
import os

TIME = [12, 31]

NINDEX=1

def nextFile(cFile):
    fileName = ""
    oFileName = cFile[2:]
    y = oFileName[:2]
    m = oFileName[2:4]
    d = oFileName[4:6]
    date = datetime.datetime(year=2000+int(y),month=int(m),day=int(d))
    date+=datetime.timedelta(days=1)
    y = str(date.year)[2:]
    m = str(date.month)
    d = str(date.day)
    if len(m)==1:
        m = '0'+m
    if len(d)==1:
        d = '0'+d
    toReturn = 'sp'+y+m+d+'.txt'
    while True:
        if os.path.isfile("dataset/"+toReturn):
            break
        else:
            date+=datetime.timedelta(days=1)
            y = str(date.year)[2:]
            m = str(date.month)
            d = str(date.day)
            if len(m)==1:
                m = '0'+m
            if len(d)==1:
                d = '0'+d
            toReturn = 'sp'+y+m+d+'.txt'
    return toReturn

def namesList(readLines):
    NAMES = []
    IN=readLines
    for i in IN:
        j = i.split(",")
        NAMES.append([j[0], float(j[1]), float(j[2])])
    return NAMES

# FILENAME[0]="sp080307"
# INDATAA=open("dataset/"+FILENAME[0]+".txt", 'r')
# INDATAAFORMAT = INDATAA.readlines()
# for i in range(len(INDATAAFORMAT)):
#     INDATAAFORMAT[i]=INDATAAFORMAT[i].split(",")
# INPUT = []
# for i in range(len(INDATAAFORMAT)):
#     INAPP = (float(INDATAAFORMAT[i][5])/float(INDATAAFORMAT[i][2])-1)*100
#     INPUT.append(INAPP)
#     #print INAPP
# SM=Net(id="SSIM001")
# OUT = SM.forward(INPUT)
# OUT2 = []
# for i in OUT:
#     print i, (i-0.5)*2.0
#     OUT2.append((i-0.5)*2.0)
#
# FILENAME[0]="sp080310"
# INDATAB=open("dataset/"+FILENAME[0]+".txt", 'r')
# INDATABFORMAT = INDATAB.readlines()
# for i in range(len(INDATABFORMAT)):
#     INDATABFORMAT[i]=INDATABFORMAT[i].split(",")
# for i in range(len(INDATABFORMAT)):
#     print INDATAAFORMAT[i][5], INDATABFORMAT[i][2], (float(INDATAAFORMAT[i][5])*(1+OUT2[i]))

def fileRead(filename):
    #print "Reading:", filename
    cfile = open(filename, 'r')
    x=cfile.readlines()
    cfile.close()
    y=[]
    for i in x:
        y.append(i.split(","))
    z=[]
    for j in y:
        z.append([j[1], float(j[2]), float(j[5])])
    return z

def scanFile(file, name):
    x = open(file)
    a = x.readlines()
    x.close()
    b=[]
    for i in a:
        b.append(i.split(','))
    for i in b:
        if i[1] == name:
            return i
    return 'noName'

# namelist = open("nameList.txt", 'r')
# nnList=namelist.readlines()
# namelist.close()
# nlist = []
# for i in nnList:
#     nlist.append(i.replace("\n", ""))
#
# files = []
#
# a= os.listdir("datasetformatted")
#
# for i in a:
#     a = open("datasetformatted/"+i,'r')
#     length=len(a.readlines())
#     print length
#     a.close()

# for i in a:
#     files.append([i,fileRead("dataset/"+i)])
#
# for i in files:
#     name = i[0]
#     count = 0
#     temp = open("datasetformatted/"+name, 'w')
#     for j in nlist:
#         found = False
#         writeVal = ""
#         for k in i[1]:
#             if j == k[0]:
#                 found = True
#                 writeVal=k[0]+","+str(k[1])+","+str(k[2])
#                 break
#         if not found:
#             index = files.index(i)
#             while True:
#                 if index == len(files)-1:
#                     index=-1
#                 cFile2=files[index+1]
#                 name2=cFile2[0]
#                 data2=cFile2[1]
#                 shouldBreak=False
#                 #print "Index:", index, name2
#                 for l in data2:
#                     #print "J:L::", name2,j, l[0]
#                     if j == l[0]:
#                         writeVal=l[0]+","+str(l[1])+","+str(l[2])
#                         shouldBreak=True
#                         break
#                 if shouldBreak:
#                     #print "Found. Breaking."
#                     break
#                 index+=1
#         #print writeVal
#         temp.write(writeVal+"\n")
#     print name, len(i[1]), len(nlist), count
#     temp.close()

# NAMES = []
# IN=open("dataset/"+f1, 'r').readlines()
# for i in IN:
#     j = i.split(",")
#     NAMES.append([j[1], 1])
# f1 = nextFile(f1)
# while True:
#     print f1
#     IN=open("dataset/"+f1, 'r')
#     for i in IN:
#         j = i.split(",")[1]
#         test = False
#         for i in NAMES:
#             if j != i[0]:
#                 continue
#             else:
#                 NAMES[NAMES.index(i)][1]+=1
#                 test = True
#                 break
#         if not test:
#             NAMES.append([j, 1])
#     if f1 == "sp100820.txt":
#         break
#     f1 = nextFile(f1)
# for i in NAMES:
#     print i
# print len(NAMES)
# a=open("nameList.txt", 'w')
# for i in NAMES:
#     a.write(i[0]+"\n")
# exit()

errx=0.1
thresh=75
countx=0
NETID = "SIM1v3n003"
f1 = 'sp080225.txt'

SM=Net(id=NETID, sizes=[579, 579,579,579, 579])
if not os.path.exists("data/SIM1/"+NETID):
    os.makedirs("data/SIM1/"+NETID)

while True:
    print "MESSAGE: Current file: " + f1 + "."
    inputFileA=open("datasetformatted/" + f1, 'r')
    inputFileB=open("datasetformatted/" + nextFile(f1), 'r')

    try:
        fileA = namesList(inputFileA.readlines())
        fileB = namesList(inputFileB.readlines())

        inputFileA.close()
        inputFileB.close()

        INPUT = []
        OUTPUT = []
        for i in range(len(fileA)):
            INAPP = (float(fileA[i][2]) / float(fileA[i][1]) - 1) * 100
            OUTAPP = ((float(fileB[i][1]) / float(fileA[i][2]) - 1) / 2.0) + 0.5
            INPUT.append(INAPP)
            OUTPUT.append(OUTAPP)
        print "DEBUG: Porpagating with constant", errx, "."
        SM.backprop(INPUT, OUTPUT, K=errx)
        ###---------------

        OUT = SM.forward(INPUT)
        OUT2 = []
        for i in OUT:
            OUT2.append((i-0.5)*2.0)

        inputFileB=open("datasetformatted/" + nextFile(f1), 'r')
        fileB = namesList(inputFileB.readlines())
        count = [0, 0, 0]
        for i in range(len(fileB)):
            direction = False

            if (((float(fileA[i][2])*(1+OUT2[i]))) < float(fileA[i][2])) and (float(fileB[i][1]) < float(fileA[i][1])):
                direction = True
            elif (((float(fileA[i][2])*(1+OUT2[i]))) > float(fileA[i][2])) and (float(fileB[i][1]) > float(fileA[i][1])):
                direction = True
            else:
                direction = False
            if direction:
                count[0]+=1
                count[2] += abs(float(fileB[i][1]) - (float(fileA[i][2]) * (1 + OUT2[i])))
            else:
                count[1]+=1
        print "DEBUG: ", 100*float(count[0])/float(len(fileB)), 100 * float(count[1]) / float(len(fileB)), count[2] / float(count[0])

        if 100*float(count[0])/float(len(fileB)) > thresh:
            VX = SM
            VX.ID = NETID+"/"+NETID+"_"+str(countx)
            VX.save()
            countx+=1

        errx = (count[2]/float(count[0]))/100

        a=open("data/SIM1/"+NETID+"/Error.txt", 'a')
        b=open("data/SIM1/"+NETID+"/True.txt", 'a')
        c=open("data/SIM1/"+NETID+"/False.txt", 'a')

        a.write(str(count[2]/float(count[0]))+'\n')
        b.write(str(100 * float(count[0]) / float(len(fileB))) + '\n')
        c.write(str(100 * float(count[1]) / float(len(fileB))) + '\n')

        a.close()
        b.close()
        c.close()

        ###---------------
        try:
            SM.save()
            print "MESSAGE: Iteration Successful. Continuing..."
        except:
            print "CRITICAL ERROR: Saving failed. Exiting cleanly."
            exit()
    except:
        print "ERROR: Unknown error during runtime."

    f1 =nextFile(f1)
    #if f1 == "sp100820.txt":
    #    print "MESSSAGE: Finished."
    #    break

#exit()

# f1 = 'sp080225.txt'
#
# INDATAA=open("dataset/"+f1, 'r')
# INDATAAFORMAT = INDATAA.readlines()
# for i in range(len(INDATAAFORMAT)):
#     INDATAAFORMAT[i]=INDATAAFORMAT[i].split(",")
# INPUT = []
# for i in range(len(INDATAAFORMAT)):
#     INAPP = (float(INDATAAFORMAT[i][5])/float(INDATAAFORMAT[i][2])-1)*100
#     INPUT.append(INAPP)
#     #print INAPP
# SM=Net(id=NETID)
# print SM.Size
# OUT = SM.forward(INPUT)
# OUT2 = []
# for i in OUT:
#     #print i, (i-0.5)*2.0
#     OUT2.append((i-0.5)*2.0)
#
# INDATAB=open("dataset/"+nextFile(f1), 'r')
# INDATABFORMAT = INDATAB.readlines()
# for i in range(len(INDATABFORMAT)):
#     INDATABFORMAT[i]=INDATABFORMAT[i].split(",")
# count = [0, 0, 0]
# for i in range(len(INDATABFORMAT)):
#     direction = False
#
#     if (((float(INDATAAFORMAT[i][5])*(1+OUT2[i]))) < float(INDATAAFORMAT[i][5])) and (float(INDATABFORMAT[i][2]) < float(INDATAAFORMAT[i][5])):
#         direction = True
#     elif (((float(INDATAAFORMAT[i][5])*(1+OUT2[i]))) > float(INDATAAFORMAT[i][5])) and (float(INDATABFORMAT[i][2]) > float(INDATAAFORMAT[i][5])):
#         direction = True
#     else:
#         direction = False
#     if direction:
#         count[0]+=1
#         count[2] += abs(float(INDATABFORMAT[i][2]) - (float(INDATAAFORMAT[i][5])*(1+OUT2[i])))
#     else:
#         count[1]+=1
#     print INDATAAFORMAT[i][5], INDATABFORMAT[i][2], (float(INDATAAFORMAT[i][5])*(1+OUT2[i])), direction
# print 100*float(count[0])/float(len(INDATABFORMAT)), 100*float(count[1])/float(len(INDATABFORMAT)), count[2]/float(count[0])

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
