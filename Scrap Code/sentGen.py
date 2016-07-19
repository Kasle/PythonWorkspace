a = open('input.txt','r')
b = a.readlines()
print b
c = []
wordList = []
for i in b:
    for j in i.split(" "):
        
