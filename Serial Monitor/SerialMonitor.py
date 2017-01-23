import serial
import datetime
import sys

print "-START-",str(datetime.datetime.now())[0:19]

port = ''
for i in range(5):
    try:
        port = int(raw_input("Port (#): "))
    except:
        if i >= 4: print "Invalid ports given.\nPress any key to exit."; raw_input();exit()
        print "Please enter a valid port number. (" + str(4-i) + ") Attempts remain."
        continue
    port = str(port)
    break

ser = ""
print "Connecting to port COM" + port + "."

for i in range(5):
    try:
        ser = serial.Serial('COM' + port, 57600)
        print "Connection to port COM" + port + " successfill."
        break
    except:
        if i >= 4: print "Error connecting to COM"+port+".\nPress any key to exit."; raw_input();exit()
        print "Error connecting to COM"+port+". Attempting to reconnect. (" + str(4-i) + ") Attempts remain."

eCount = 0

ser.flush()


while True:
    currentTime = str(datetime.datetime.now()).split(" ")[1][0:10]
    try:
        serialOutput = ser.readline().strip()
        print serialOutput
    except KeyboardInterrupt:
        print "\nExiting."
        f.close()
        break
    except:
        print "Unexpected error:",sys.exc_info()[0]
        if eCount >=  5: print "Press any key to exit."; raw_input();break
        eCount+=1
        print "("+str(5-eCount)+") Attempts remain."

