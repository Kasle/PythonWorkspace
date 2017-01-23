import time

timeout = 0.1

def bfrun(inp, memCount = 256):
    startTime = time.time()
    
    memList = [0 for i in range(memCount)]

    inputString = inp

    inputString = list(inputString)

    success = True

    memIndex = 0
    loopIndex = 0
    loopDepth = 0

    prnt = ""
    shouldNotKill = True

    try:
        
        while (loopIndex < len(inputString)) and shouldNotKill:
            if (time.time()-startTime) > timeout:
                success = False
                shouldNotKill = False
                break
            if loopDepth < 0:
                success = False
                shouldNotKill = False
                break
            
            cmd = inputString[loopIndex]

            if cmd == ">":
                memIndex+=1
                if memIndex > len(memList)-1:
                    success = False
                    break
            elif cmd == "<":
                memIndex-=1
                if memIndex < 0:
                    success = False
                    break
            elif cmd == "+":
                memList[memIndex]+=1
            elif cmd == "-":
                memList[memIndex]-=1
            elif cmd == ".":
                prnt+=chr(memList[memIndex])
            elif cmd == "[":
                loopDepth += 1
            elif cmd == "]":
                loopDepth -= 1
                loopID = 0
                loop = True
                if memList[memIndex] == 0:
                    loop = False
                while loop:
                    if (time.time()-startTime) > timeout:
                        success = False
                        shouldNotKill = False
                        break
                
                    if inputString[loopIndex] == "]":
                        loopID += 1
                    elif inputString[loopIndex] == "[":
                        loopID -= 1

                    if loopID == 0:
                        break

                    loopIndex -= 1
            
            loopIndex+=1
    except:
        success =False

    if loopDepth != 0:
        success = False
    
    return [prnt, memList, success, time.time() - startTime]
    
