class Evolution:
    Stage = 0
    Name = "Null"
    MinLevel = "Null"
    Extras = "Null"

    def __init__(self):
        self.reset()
        
    def reset(self):
        self.Stage = 0
        self.Name = "Null"
        self.MinLevel = "Null"
        self.Extras = "Null"

    def declareJson(self):
        Stage = {}
        Stage['Number'] = self.Stage
        Stage['Name'] = self.Name
        if self.MinLevel != "Null":
            Stage['MinLevel'] = self.MinLevel
        if self.Extras != 'Null':
            Stage['Extras'] = self.Extras

    def toString(self):
        print(str(self.Stage) + " " + self.Name + " " + str(self.MinLevel) + " " + self.Extras)

    def toArray(self):
        return [self.Stage, self.Name, self.MinLevel, self.Extras]