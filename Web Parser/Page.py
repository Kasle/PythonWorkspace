__author__ = 'aleks_000'

import sys

CHAR = sys.stdin.readlines()
LEN = int(CHAR.pop())

CHAR = " ".join(CHAR).translate(None, ',./:"|[]{}!<>?;()').replace("\n", "")

SET = filter(None, CHAR.split(" "))

print SET

STRDATA = []
NUMDATA = []

for i in range(LEN):
    for j in range(len(SET) - i):
        A = " ".join(SET[j:j + i + 1])

        if A.isupper():
            if A in STRDATA:
                NUMDATA[STRDATA.index(A)] += 1
            else:
                STRDATA.append(A)
                NUMDATA.append(int("1"))
        else:
            if A.lower() in STRDATA:
                NUMDATA[STRDATA.index(A.lower())] += 1
            else:
                STRDATA.append(A.lower())
                NUMDATA.append(int("1"))

TOCHECK = open("COMMON.txt", "r")
CHECK = TOCHECK.readlines()

TOTALPRE = sum(NUMDATA)

NUMDATAT = []
STRDATAT = []

for a in STRDATA:
    if not a.isupper():
        if (a.lower() + "\n" not in CHECK):
            NUMDATAT.append(NUMDATA[STRDATA.index(a)])
            STRDATAT.append(STRDATA[STRDATA.index(a)].replace("\x81F", "'").replace("\x81f", "'"))
    else:
        if (a + "\n" not in CHECK):
            NUMDATAT.append(NUMDATA[STRDATA.index(a)])
            STRDATAT.append(STRDATA[STRDATA.index(a)].replace("\x81F", "'").replace("\x81f", "'"))

NUMDATA = NUMDATAT
STRDATA = STRDATAT

TOCHECK.close()

NUMDATA, STRDATA = zip(*sorted(zip(NUMDATA, STRDATA), reverse=True))

# print NUMDATA, STRDATA, sum(NUMDATA)

TOTAL = sum(NUMDATA)

print "> Total Words: " + str(TOTALPRE)
print "> Total Words After Common Removal: " + str(TOTAL)

INDEX = 0
MAX = (float(NUMDATA[0]) / TOTAL) * 100

# print NUMDATA, STRDATA, sum(NUMDATA)

while True:
    if (float(NUMDATA[INDEX]) / NUMDATA[0]) > 0.05:
        X = int((float(NUMDATA[INDEX]) / TOTAL) * 100)
        Y = int((float(NUMDATA[INDEX]) / NUMDATA[0]) * 100)
        print "> -" + (Y)*"#" + (101-Y)*"=" + " : " + str((float(NUMDATA[INDEX]) / TOTAL) * 100.0)[:4] + "% : " + str(NUMDATA[INDEX]) + " : " + (STRDATA[INDEX].upper())
    else:
        print "> EXIT : Tolerance Reached"
        break

    INDEX += 1
    if INDEX == len(NUMDATA):
        print "> EXIT : End of Data Reached"
        break


