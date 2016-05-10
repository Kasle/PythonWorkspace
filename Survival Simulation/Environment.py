__author__ = 'aleks_000'

import math
import Critter
import random

def fitnessFunction(weights, stats, g):
    _sum = 0

    weights[0]=10*math.sin(math.sin(g/10.0)*math.sin(g/20.0))
    weights[2]=(-5*math.sin(g/5.0))

    for w in weights:
        _sum += w * stats[weights.index(w)]

    return _sum

print "SIMULATION INFORMATION:"
_stNum = int(input("Starting Population: "))
_genNum = int(input("Total Generations: "))
print "WEIGHT, STRENGTH, SPEED, AGILITY:"
_weights = input("Fitness Weights: ")

_ECO = []
for i in range(0, _stNum):
    _ECO.append(Critter.Critter([]))

for Generation in range(1, _genNum + 1):
    if len(_ECO) == 0:
        print "EXTINCT:"
        break

    _fitness = []
    _fitECO = []

    for Organism in _ECO:
        #print Organism.getGenes()
        _tempFit = fitnessFunction(_weights, Organism.getGenes(), Generation)
        if  len(_fitECO) == 0:
            _fitECO.append([_tempFit, Organism])
        else:
            app = False
            for i in range(len(_fitECO)):
                if _tempFit > _fitECO[i][0]:
                    #print _fitECO
                    _fitECO.insert(i, [_tempFit, Organism])
                    app = True
                    #print _fitECO
                    break
            if not app:
                _fitECO.append([_tempFit, Organism])

    _ECO = []

    if len(_fitECO) > 10:
        _fitECO = _fitECO[0:9]

    #print _fitECO

    print str(Generation) + ", " + str(_fitECO[0][1].getGenes()).replace("[", "").replace("]", "")

    for i in range(1,len(_fitECO)):
        _ECO+=_fitECO[i][1].mate(_fitECO[0][1])





























