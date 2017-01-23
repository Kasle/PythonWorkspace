patt = (raw_input("Pattern"))

width = int(raw_input("Width"))
length = int(raw_input("Length"))

mult = int((width * length ) / float(len(patt)))

patt *= mult

count = 0

for i in range(0, length):
    print patt[i*width:i*width+width]
    count+=1
raw_input()