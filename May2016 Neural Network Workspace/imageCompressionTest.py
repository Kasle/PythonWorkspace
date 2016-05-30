from PIL import Image


IM = Image.open("IInput\\Birds\\1.bmp")
nN=(50, 50)
IM = IM.resize(nN, Image.ANTIALIAS)
IM.show()