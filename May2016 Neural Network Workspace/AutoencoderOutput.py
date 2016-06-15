import NNetwork
from PIL import Image 
from time import time

pSize = 100

Net = NNetwork.Network("AutoencoderLettervShape")

A = Image.open("AInput.jpg")
A.show()

AP = [sum(i)/765.0 for i in list(A.getdata())]

oPix = Net.forward([0]*(pSize**2))
tOut = []
for j in oPix:
    val = int(255 * j)
    tOut+=[(val, val, val)]
t = Image.new('RGB', (pSize, pSize))
t.putdata(tOut)
t.show()