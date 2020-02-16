class Capabilities:
    Overland = 0
    Sky = 0
    Swim = 0
    Levitate = 0
    Burrow = 0
    JumpH = 0
    JumpL = 0
    Power = 0
    WeightClass = 0
    Naturewalk = []
    Other = []
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.Overland = 0
        self.Sky = 0
        self.Swim = 0
        self.Levitate = 0
        self.Burrow = 0
        self.JumpH = 0
        self.JumpL = 0
        self.Power = 0
        self.WeightClass = 0
        self.Naturewalk = []
        self.Other = []

    def declareJson(self):
        Capabilities = {}
        Capabilities['Overland'] = self.Overland
        Capabilities['Sky'] = self.Sky
        Capabilities['Swim'] = self.Swim
        Capabilities['Levitate'] = self.Levitate
        Capabilities['Burrow'] = self.Burrow
        Capabilities['JumpH'] = self.JumpH
        Capabilities['JumpL'] = self.JumpL
        Capabilities['Power'] = self.Power
        Capabilities['Naturewalk'] = self.Naturewalk
        Capabilities['Other'] = self.Other