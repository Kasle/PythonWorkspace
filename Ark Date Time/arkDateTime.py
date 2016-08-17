class time: #Main Class
    def __init__(self, time = "00:00:00"): #Create blank time, user input
        self.t = time #Set variables
        self.s = float(time.split(":")[2])
        self.m = int(time.split(":")[1])
        self.h = int(time.split(":")[0])
        
    def __add__(self, other): #Adding time (Main use)
        returnTime = time(self.t)
        returnTime.s+=other.s #Add variables from other time
        returnTime.m+=other.m
        returnTime.h+=other.h
        
        #print returnTime.s, returnTime.m, returnTime.h
        
        if returnTime.s >= 60: #Crop seconds
            tmin = int(returnTime.s / 60)
            returnTime.s-=60 * (tmin)
            returnTime.m+=tmin
            
        #print returnTime.s, returnTime.m, returnTime.h
        
        if returnTime.m >= 60: #Crop minutes
            thour = (returnTime.m / 60)
            returnTime.m-=60 * (thour)
            returnTime.h+=thour
        
        #print returnTime.s, returnTime.m, returnTime.h        
        
        if returnTime.h >= 24: #Crop hours
            hmult = returnTime.h / 24
            returnTime.h-=24 * hmult
        returnTime.update() #Update string
        return returnTime #Return the new time
    
    def __sub__(self, other): #Subtract two times
        returnTime = time(returnTime.t)
        returnTime.s -= other.s
        returnTime.m -= other.m
        returnTime.h -= other.h
        
        mult = abs(int(returnTime.s / 60)) #rectify and crop seconds, minutes, and hours
        returnTime.s += 60 * mult
        if returnTime.s < 0:
            returnTime.s+=60
            mult+=1
        returnTime.m -= mult
        
        mult = abs(int(returnTime.m / 60))
        returnTime.m += 60 * mult
        if returnTime.m < 0:
            returnTime.m+=60
            mult+=1
        returnTime.h -= mult
        
        mult = abs(int(returnTime.h / 24))
        returnTime.h += 24 * mult
        if returnTime.h < 0:
            returnTime.h+=24
        
        returnTime.update() #Update string
        
        return returnTime #Return
        
    def __str__(self): #Print function
        self.update()
        return self.t
        
    def update(self): #Update string from stored values
        ts = str(self.s)
        if len(ts.split(".")[0]) < 2:
            ts = "0"+ts
        tm = str(self.m)
        if len(tm) < 2:
            tm = "0"+tm
        th = str(self.h)
        if len(th) < 2:
            th = "0"+th
        self.t = str(th)+":"+str(tm)+":"+str(ts)
        
###
###Example Of Use
###        
        
#a = time("22:00:55")
#b = time("00:00:1")
#
#print a, b
#
#print a + b
#
#print a, b
#    