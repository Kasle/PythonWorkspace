import math

class resourceSim:
    levels = {
        'M' : 0,
        'C' : 0,
        'D' : 0,
        'S' : 0,
        }

    cost = {
        'mMm' : 0,
        'mCm' : 0,
        'mDm' : 0,
        'mSm' : 0,
        'mMc' : 0,
        'mCc' : 0,
        'mDc' : 0,
        'mSc' : 0,
        'sMm' : 0,
        'sCm' : 0,
        'sDm' : 0,
        'sMc' : 0,
        'sCc' : 0,
        'sDc' : 0,
        }
    
    storage = {
        'M' : 0,
        'C' : 0,
        'D' : 0,
        }

    production = {
        'M' : 0,
        'C' : 0,
        'D' : 0,
        'S' : 0,
        }

    usage = {
        'M' : 0,
        'C' : 0,
        'D' : 0,
        }

    A = 1
    
    def __init__(self, mL, mS, cL, cS, dL, dS, sL, A):
        self.A = A
        
        self.levels['M'] = mL
        self.levels['C'] = cL
        self.levels['D'] = dL
        self.levels['S'] = sL

        self.storage['M'] = mS
        self.storage['C'] = cS
        self.storage['D'] = dS

        self.updateProduction()
        #self.updateCost()

    def updateProduction(self):
        self.production['M'] = int(self.A * 30 * self.levels['M'] * 1.1 ** self.levels['M']) + 90
        self.production['C'] = int(self.A * 20 * self.levels['C'] * 1.1 ** self.levels['C']) + 46
        self.production['D'] = int(self.A * 10 * self.levels['D'] * 1.1 ** self.levels['D'] * (1.36-0.004*-6))
        #production['S'] =

    #def updateCost(self):
        #cost[''] =
        #cost[''] =

        #cost[''] =
        #cost[''] =

        #cost[''] =
        #cost[''] =

        #cost[''] =
        #cost[''] =

        #cost[''] =
        #cost[''] =

        #cost[''] =
        #cost[''] =

        #cost[''] =
        #cost[''] = 
