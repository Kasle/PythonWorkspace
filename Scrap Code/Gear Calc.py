import math
while True:
    minSize = input("Enter Minimum # of Gear Teeth: ")
    maxSize = input("Enter Maximum # of Gear Teeth: ")
    inRPM = float(input("Enter Input RPM: "))
    outRPM = float(input("Enter Output RPM: "))
    maxError = float(input("Enter Max Error: "))
    for A in range (minSize, maxSize+1):
        for B in range (minSize, maxSize+1):
            for C in range (minSize, maxSize+1):
                for D in range (minSize, maxSize+1):
                    A=float(A)
                    B=float(B)
                    C=float(C)
                    D=float(D)
                    Error = (((inRPM/((B/A)*(D/C))) - (outRPM))**2)**0.5
                    if (Error <= maxError):
                        print int(A), int(B), int(C), int(D)
    print " "
    
