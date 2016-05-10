import random
import math


class Critter:
    def __init__(self, _genome):
        if _genome == []:
            self._genes = [random.normalvariate(0, 1),
                           random.normalvariate(0, 1),
                           random.normalvariate(0, 1),
                           random.normalvariate(0, 1),
                           random.normalvariate(0, 0.05),
                           random.normalvariate(0, 0.2)]
        else:
            self._genes = _genome
        self.mutate()

    def getGenes(self):
        return self._genes

    def mate(self, _mate):
        self.ofSpr = []
        for ofSNum in range(0, random.randint(5, 11)):
            self.tempGenes = []
            for i in range(0, len(_mate.getGenes())):
                if random.random() < 0.5:
                    self.tempGenes.append(self._genes[i])
                else:
                    self.tempGenes.append(_mate.getGenes()[i])
            self.ofSpr.append(Critter(self.tempGenes))
        return self.ofSpr

    def mutate(self):
        for _gene in range(0, len(self._genes)-2):
            if random.random() < self._genes[-1]:
                self._genes[_gene] += random.normalvariate(0, self._genes[-2])

            if random.random() < 0.001:
                self._genes[_gene] = -self._genes[_gene]
