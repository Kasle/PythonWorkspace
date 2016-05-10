import math

def r(string, a, w = "",s=""):
    for i in range(len(string)):
        if s=="":
            w=""
        w+=string[i]
        if len(string) == 1:
            a.append(w)
        else:
            r(string.replace(string[i], ""), a, w, string)
            w = w[:len(w) -1]

def w(name, a):
    _file = open(name + ".txt", "w")
    for i in range(0, len(a), 5):
        _file.write(a[i] + " " + a[i+1] + " " + a[i+2] + " " + a[i+3] + " " + a[i+4] + "\n")
    _file.close()
