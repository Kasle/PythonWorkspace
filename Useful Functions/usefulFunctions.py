def addTime(tStart, tAdd): # Eg. ("11:25:03", "00:01:05"), ("HH:MM:SS","HH:MM:SS" to add)
    TIME = tStart.split(":")
    TIME = [float(TIME[0]),float(TIME[1]),float(TIME[2])]
    NEWTIME = [0,0,0]
    TADD = tAdd.split(":")
    TADD = [float(TADD[0]),float(TADD[1]),float(TADD[2])]
    NEWTIME[2] += (TIME[2] + TADD[2])
    if NEWTIME[2] >= 60:
        NEWTIME[2] -= 60
        TADD[1]+=1
    NEWTIME[1] += (TIME[1] + TADD[1])
    if NEWTIME[1] >= 60:
        NEWTIME[1] -= 60
        TADD[0]+=1
    NEWTIME[0] += (TIME[0] + TADD[0])
    if NEWTIME[0] >= 24:
        NEWTIME[0] -= 24
    NEWTIME = [str(int(NEWTIME[0])),str(int(NEWTIME[1])),str(NEWTIME[2])]
    for i in range(len(NEWTIME)):
        if len(NEWTIME[i])  == 1 or (i == 2 and NEWTIME[i][1] == "."):
            NEWTIME[i] = "0"+NEWTIME[i]
	return ":".join(NEWTIME)

def timeToCode(spl): # Eg. [2000, 12, 03, 23, 13, 04], [YYYY, MM, DD, HH, mm, SS]
	newValue = 38064000*float(spl[0])+2928000*float(spl[1])+91500*float(spl[2])+3660*float(spl[3])+60*float(spl[4])+float(spl[5])