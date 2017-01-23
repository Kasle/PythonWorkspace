toprint = []
temp = raw_input("all: ")
toprint.append("all: " + temp)

bases = temp.split(' ')

while 1:
    if not len(bases):
        break
    base = bases.pop(0)
    temp = raw_input(base + ": ")
    if len(temp):
        bases+=temp.split(" ")
        toprint.append(base + ": " + temp)
        while 1:
            added = raw_input("\t")
            if len(added):
                toprint.append("\t"+added)
            else:
                break
print "clean:"
toprint.append("clean:")
while 1:
    added = raw_input("\t")
    if len(added):
        toprint.append("\t"+added)
    else:
        break

f = open("makefile", 'w')
for i in toprint:
    f.write(i+"\n")
f.close()

