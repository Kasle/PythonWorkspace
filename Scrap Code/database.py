import random
class database:
        def __init__(self):
                self.__integer1 = 1
                self.__integer2 = 4
                self.__string1 = "Cats"
                self.__string2 = "Dogs"
                self.__float1 = 0.145
                self.__float2 = 3.782
                self.__list2 = ["cat", "dog", "fish", "hamster", "bird"]
                self.__list3 = ["Emma", "Noah", "Olivia", "Liam"]
                self.__list1 = [[random.randint(0, 3) for i in range(len(self.__list2))] for j in range(len(self.__list3))]

        def getInt1(self):
                return self.__integer1

        def getInt2(self):
                return self.__integer2

        def getString1(self):
                return self.__string1

        def getString2(self):
                return self.__string2

        def getFloat1(self):
                return self.__float1

        def getFloat2(self):
                return self.__float2

        def getPets(self):
                return self.__list2

        def getNames(self):
                return self.__list3

        def getCounts(self):
                return self.__list1

        def checkIntAnswer(self, answer):
                try:
                        if answer == self.__integer1 + (5 * self.__integer2):
                                return True
                        return False
                except:
                        return False

        def checkFloatAnswer(self, answer):
                try:
                        if answer == ((self.__float1 / self.__float2) * self.__integer1):
                                return True
                        return False
                except:
                        return False

        def checkStringAnswer(self, answer):
                try:
                        if answer == (self.__string1 + " and " + self.__string2 + " are great!"):
                                return True
                        return False
                except:
                        return False

        def checkListAnswer(self, name, answer):
                try:
                        workingName = self.__list3.index(name)
                        tName = self.__list3[workingName]
                        petList = self.__list1[workingName]
                        tAnswer = tName + " has"
                        for i in range(len(petList)):
                                if petList[i] == 1:
                                        tAnswer += " " + str(petList[i]) + " " + self.__list2[i] + ","
                                else:
                                        tAnswer += " no " + self.__list2[i] + ","
                        tAnswer = tAnswer[0:-1]
                        tAnswer+="."
                        if tAnswer == answer:
                                return True
                        return False
                except:
                        return False

        def getQuestions(self):
                print "1. First integer plus 5 times the second integer. Check your answer with 'checkIntAnswer'.\n"
                print "2. Animal 1 and Animal 2 are great! Check your answer with 'checkStringAnswer'.\n"
                print "3. Float 1 divided by Float 2, then multiplied by Integer 1. Check your answer with 'checkFloatAnswer'.\n\n"
                print "4. People and the animals they own in the following format:"
                print "<Name> has <#> <Animal>, <#> <Animal>, ..., <#> <Animal>.\n"
                print "If the person has no animal, replace <#> with the string 'no'.\n"
                print "Example:"
                print "Mark has 1 snake, no cat, 5 fish."
