import random


class Individual:
    deathRateM = [177, 4386, 8333, 1908, 1215, 663, 279, 112, 42, 15, 6]
    deathRateF = [277, 5376, 10417, 4132, 2488, 1106, 421, 178, 65, 21, 7]
    birthRate = [866, 119757, 444300, 641377, 603041, 261885, 58627, 4191]
    tBirthS = 2999820

    ageD = [0, 1, 5, 15, 25, 35, 45, 55, 65, 75, 85]
    ageB = [12, 15, 20, 25, 30, 35, 40, 45, 50]

    def __init__(self, name, age=0):
        if random.random() < 0.51:
            self.sex = "M"
        else:
            self.sex = "F"

        self.name = name

        if age < 0:
            self.age = 0
        else:
            self.age = int(age)

    def AGE(self):
        return True

    # def BIRTH(self):
    #     if self.sex == "M" or findBirthIndex() == -1:
    #         return False
    #     if birthRate[findBirthIndex()] / tBirths:
    #     return shouldBirth

    def findDeathIndex(self):
        index = 0
        for i in range(len(self.ageD) - 1, 0, -1):
            if self.age >= self.ageD[i]:
                index = i
                break
        return index

    def findBirthIndex(self):
        index = 0
        if self.sex == "M" or self.age < 12 or self.age >= 60:
            index = -1
            return index

        for i in range(len(self.ageB) - 1, 0, -1):
            if self.age >= self.ageB[i]:
                index = i
                break
        return index
