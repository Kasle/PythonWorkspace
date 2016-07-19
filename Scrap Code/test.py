from database import database as blackBox
data = blackBox()
data.getQuestions()
print "\n-----------------------------------------------------------------------\n"

##------------------------------------------------------------------------

x = data.getInt1()
y = data.getInt2()
z = x+(5*y)

answer = 0
print data.checkIntAnswer(z)

##----

print data.getString1()
print data.getString2()

x = data.getString1() + " and " + data.getString2() + " are great!"
print x

print data.checkStringAnswer(x)

##-----------------

x = data.getFloat1()
y = data.getFloat2()
z = data.getInt1()

j = (x/y)*z

print data.checkFloatAnswer(j)


print data.getNames()
print data.getPets()
print data.getCounts()

##for element in data.getNames():
##    name = element
##    print name 
    
for index in range(len(data.getNames())):
    output = data.getNames()[index] + " has "
    
    numListAnimals = data.getCounts()[index]
    for numberIndex in range(len(numListAnimals)):
        pet = data.getPets()[numberIndex]
        tempAdd = ""
        if numListAnimals[numberIndex] == 0:
            tempAdd += "no"
        else:
            tempAdd += str(numListAnimals[numberIndex])
        output += tempAdd + " " + data.getPets()[numberIndex] + ", "
                    
    print output[0:-2] + "."
