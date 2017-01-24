import time

timeout = 0.05

def bfrun(inp, memCount = 256):
    
    
    memList = [0 for i in range(memCount)]
    
    inputString = list(inp)

    memIndex = 0
    loopIndex = 0
    loopDepth = 0

    prnt = ""

    errCount = 0
    for i in inputString:
        if i == "[":
            errCount+=1
        elif i == "]":
            errCount-=1
    
    if errCount: return ['', 'bracket error']

    startTime = time.time()
    while (loopIndex < len(inputString)):
        if (time.time()-startTime) > timeout:
            return ['', 'timeout'];
        
        cmd = inputString[loopIndex]
        #print(cmd, loopDepth)
        
        if cmd == ">":
            memIndex+=1
            if memIndex > len(memList)-1:
                memIndex = len(memList)-1
        elif cmd == "<":
            memIndex-=1
            if memIndex < 0:
                memIndex = 0
        elif cmd == "+":
            memList[memIndex]+=1
            if memList[memIndex] > 255:
                memList[memIndex] = 0
        elif cmd == "-":
            memList[memIndex]-=1
            if memList[memIndex] < 0:
                memList[memIndex] = 255
        elif cmd == ".":
            prnt+=chr(memList[memIndex])
        elif cmd == "[":
            loopDepth += 1
        elif cmd == "]":
            loopDepth -= 1
            if loopDepth < 0:
                return ['', 'in loop bracket error']
            if memList[memIndex] == 0:
                loopIndex += 1
                continue
            loopIndex -= 1
            loopID = 1
            
            while 1:
                if (time.time()-startTime) > timeout:
                    return ['', 'infinite loop timeout'];
            
                if inputString[loopIndex] == "]":
                    loopID += 1
                elif inputString[loopIndex] == "[":
                    loopID -= 1
                loopIndex -= 1
                if loopID == 0:
                    break

                
        
        loopIndex+=1
    
    return [prnt, memList]

print (bfrun(""))
