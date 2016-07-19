delim = ['.','!','?',";"]

A = open("input.txt", 'r')

read= "".join(A.readlines()).replace("\n", '').replace(":", ",").replace(".).", ").")

print read

for i in delim:
    read = read.replace(i, i+"~")

read = read.split("~")

for i in range(len(read)):
    read[i] = read[i].strip()

out = open("output.txt", 'w')

for i in read:
    out.write(i+"\n")


