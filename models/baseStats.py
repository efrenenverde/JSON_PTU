class BaseStats:
    HIT = 1
    ATK = 1
    DEF = 1
    SAT = 1
    SDE = 1
    SPD = 1
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.HIT = 1
        self.ATK = 1
        self.DEF = 1
        self.SAT = 1
        self.SDE = 1
        self.SPD = 1

    def declareJson(self):
        Stats = {}
        Stats['HP'] = self.HIT
        Stats['Attack'] = self.ATK
        Stats['Defense'] = self.DEF
        Stats['Special Attack'] = self.SAT
        Stats['Special Defense'] = self.SDE
        Stats['Speed'] = self.SPD

        return Stats