patt = "=====/"

width = 20
length = 60

mult = int((width * length ) / float(len(patt)))

patt *= mult

count = 0

for i in range(0, length):
    print patt[i*width:i*width+width]
    count+=1
    