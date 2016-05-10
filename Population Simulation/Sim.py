from Population import Individual as Ind
import random

NAME = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

startPop = input("Start Population: ")

POP =[]
for i in range(startPop):
    nameI = NAME[(random.randint(0, len(NAME)-1))]+NAME[(random.randint(0, len(NAME)-1))]+NAME[(random.randint(0, len(NAME)-1))]+NAME[(random.randint(0, len(NAME)-1))]+NAME[(random.randint(0, len(NAME)-1))]
    POP.append(Ind(nameI, random.normalvariate(25, 10)))
    print nameI, POP[i].age, POP[i].findDeathIndex(), POP[i].sex, POP[i].findBirthIndex()

