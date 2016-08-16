class time: #Main Class
    def __init__(self, time = "00:00:00"): #Create blank time, user input
        self.t = time #Set variables
        self.s = float(time.split(":")[2])
        self.m = int(time.split(":")[1])
        self.h = int(time.split(":")[0])
        
    def __add__(self, other): #Adding time (Main use)
        self.s+=other.s #Add variables from other time
        self.m+=other.m
        self.h+=other.h
        
        #print self.s, self.m, self.h
        
        if self.s >= 60: #Crop seconds
            tmin = int(self.s / 60)
            self.s-=60 * (tmin)
            self.m+=tmin
            
        #print self.s, self.m, self.h
        
        if self.m >= 60: #Crop minutes
            thour = (self.m / 60)
            self.m-=60 * (thour)
            self.h+=thour
        
        #print self.s, self.m, self.h        
        
        if self.h >= 24: #Crop hours
            hmult = self.h / 24
            self.h-=24 * hmult
        self.update() #Update string
        return self #Return the new time
    
    def __sub__(self, other): #Subtract two times
        
        self.s -= other.s
        self.m -= other.m
        self.h -= other.h
        
        mult = abs(int(self.s / 60)) #rectify and crop seconds, minutes, and hours
        self.s += 60 * mult
        if self.s < 0:
            self.s+=60
            mult+=1
        self.m -= mult
        
        mult = abs(int(self.m / 60))
        self.m += 60 * mult
        if self.m < 0:
            self.m+=60
            mult+=1
        self.h -= mult
        
        mult = abs(int(self.h / 24))
        self.h += 24 * mult
        if self.h < 0:
            self.h+=24
        
        self.update() #Update string
        
        return self #Return
        
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
#from time import sleep
#
#for i in range(24*3600):
#    print a
#    a = a + b
#    sleep(0.01)
    