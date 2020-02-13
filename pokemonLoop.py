import json
from models import capabilities
from models import baseStats

SpecialNames = ['TYPE:', 'GIRATINA', 'MR.', 'MIME', 'HOOPA', 'TAPU', 'ZYGARDE', 'MELOETTA', 'KYUREM', 'TORNADUS', 'LANDORUS', 'THUNDURUS',
    'SHAYMIN', 'ROTOM', 'DEOXYS', 'WORMADAM', 'DARMANITAN', 'LYCANROC', 'WISHIWASHI', 'MINIOR', 'NECROZMA']
NonOtherCapabilities = ['Overland', 'Sky', 'Swim', 'Levitate', 'Burrow', 'Jump', 'Power', 'Naturewalk']
Naturewalks = ['Grassland', 'Desert', 'Forest', 'Urban', 'Wetlands', 'Cave', 'Ocean', 'Mountain', 'Tundra']
SpeciesWithWeirdStats = ['PUMPKABOO', 'GOURGEIST']

class PokemonLoop:
    SpeciesName = ''
    InfoArray = []
    BaseStats = baseStats.BaseStats
    CapaList = capabilities.Capabilities


    def __init__(self, Data):
        if Data[0] not in SpecialNames:
            self.SpeciesName = Data[0]
        elif Data[0] == "JR.":
            self.SpeciesName = "MIME-JR."
        else:
            self.SpeciesName = Data[0] + '-' + Data[1]
        self.InfoArray = Data

    def resetAll(self):
        self.BaseStats.HIT = 1
        self.BaseStats.ATK = 1
        self.BaseStats.DEF = 1
        self.BaseStats.SAT = 1
        self.BaseStats.SDE = 1
        self.BaseStats.SPD = 1
        self.CapaList.Overland = 0
        self.CapaList.Sky = 0
        self.CapaList.Swim = 0
        self.CapaList.Levitate = 0
        self.CapaList.Burrow = 0
        self.CapaList.JumpH = 0
        self.CapaList.JumpL = 0
        self.CapaList.Power = 0
        self.CapaList.WeightClass = 0
        self.CapaList.Naturewalk = []
        self.CapaList.Other = []

    def setAll(self):
        self.setBaseStats()
        self.setCapabilities()

    def setBaseStats(self):
        print(self.SpeciesName)

        if self.SpeciesName in SpeciesWithWeirdStats:
            return

        i = 0
        while self.InfoArray[i] != "Base" and self.InfoArray[i+1] != "Stats:":
            i+=1
        while self.InfoArray[i] != "Basic":
            if self.InfoArray[i] == "HP:":
                self.BaseStats.HIT = int(self.InfoArray[i+1])
                self.BaseStats.ATK = int(self.InfoArray[i+3])
                self.BaseStats.DEF = int(self.InfoArray[i+5])
                self.BaseStats.SAT = int(self.InfoArray[i+8])
                self.BaseStats.SDE = int(self.InfoArray[i+11])
                self.BaseStats.SPD = int(self.InfoArray[i+13])
                i+=13
            else:
                i+=1

    # TODO: Fix this mess
    def setCapabilities(self):
        i = 0
        foundCapabilities = False
        while i < len(self.InfoArray):
            if self.InfoArray[i] == "Capability":
                i+=2
                foundCapabilities = True

            if foundCapabilities:
                if self.InfoArray[i] == 'Overland':
                    self.CapaList.Overland = int(self.InfoArray[i+1][:-1])
                elif self.InfoArray[i] == "Sky":
                    if self.InfoArray[i+1] == "Forme,":
                        print('Shaymin please stop breaking my code please')
                    elif self.InfoArray[i+1].find(',') > -1:
                        self.CapaList.Sky = int(self.InfoArray[i+1][self.InfoArray[i+1].find(',')-1])
                    else:
                        self.CapaList.Sky = int(self.InfoArray[i+1])
                elif self.InfoArray[i] == "Swim":
                    self.CapaList.Swim = int(self.InfoArray[i+1][:-1])
                elif self.InfoArray[i] == "Levitate":
                    self.CapaList.Levitate = int(self.InfoArray[i+1][:-1])
                elif self.InfoArray[i] == "Burrow":
                    self.CapaList.Burrow = int(self.InfoArray[i+1][:-1])
                elif self.InfoArray[i] == "Jump":
                    self.CapaList.JumpH = int(self.InfoArray[i+1][0])
                    self.CapaList.JumpL = int(self.InfoArray[i+1][-2])
                elif self.InfoArray[i] == "Power":
                    if self.InfoArray[i+1].find(',') > -1:
                        self.CapaList.Power = int(self.InfoArray[i+1][:-1])
                    else:
                        self.CapaList.Power = int(self.InfoArray[i+1])
                elif self.InfoArray[i] == "Naturewalk":
                    self.CapaList.Naturewalk = []
                    doneNaturewalk = self.InfoArray[i+1].find(')') > 0
                    j = 1
                    if doneNaturewalk == True:
                        self.CapaList.Naturewalk.append( self.InfoArray[i+1][1:self.InfoArray[i+j].find(')')])
                    else:
                        self.CapaList.Naturewalk.append( self.InfoArray[i+1][1:self.InfoArray[i+j].find(')')])
                        while doneNaturewalk == False:
                            j += 1
                            self.CapaList.Naturewalk.append( self.InfoArray[i+j][:self.InfoArray[i+j].find(')')] )
                            doneNaturewalk = self.InfoArray[i+j].find(')') > 0
                elif self.InfoArray[i] == "Skill":
                    break
                elif self.InfoArray[i] not in NonOtherCapabilities and ( len(self.InfoArray[i]) > 4 or self.InfoArray[i] == "Dead" ):
                    if not any(Nature in self.InfoArray[i] for Nature in Naturewalks):
                        j = 0
                        finalCapability = ""
                        if ',' not in self.InfoArray[i] and self.InfoArray[i+j+1] != "Skill":
                            finalCapability += self.InfoArray[i]
                            while ',' not in self.InfoArray[i+j] and self.InfoArray[i+j+1] != "Skill":
                                finalCapability += ' ' + self.InfoArray[i+j+1]
                                j += 1
                            finalCapability = finalCapability[:-1]
                            i += j
                        elif ',' in self.InfoArray[i]:
                            finalCapability += self.InfoArray[i][:-1]
                        else:
                            finalCapability += self.InfoArray[i]
                        self.CapaList.Other.append(finalCapability)
            i += 1

    def toJson(self):
        species = {}

        Stats = {}
        Stats['HP'] = self.BaseStats.HIT
        Stats['Attack'] = self.BaseStats.ATK
        Stats['Defense'] = self.BaseStats.DEF
        Stats['Special Attack'] = self.BaseStats.SAT
        Stats['Special Defense'] = self.BaseStats.SDE
        Stats['Speed'] = self.BaseStats.SPD

        Capabilities = {}
        Capabilities['Overland'] = self.CapaList.Overland
        Capabilities['Sky'] = self.CapaList.Sky
        Capabilities['Swim'] = self.CapaList.Swim
        Capabilities['Levitate'] = self.CapaList.Levitate
        Capabilities['Burrow'] = self.CapaList.Burrow
        Capabilities['JumpH'] = self.CapaList.JumpH
        Capabilities['JumpL'] = self.CapaList.JumpL
        Capabilities['Power'] = self.CapaList.Power
        Capabilities['Naturewalk'] = self.CapaList.Naturewalk
        Capabilities['Other'] = self.CapaList.Other

        species[self.SpeciesName] = []
        species[self.SpeciesName].append({
            '_id': self.SpeciesName,
            'Base Stats': Stats,
            'Capabilities': Capabilities
        })

        with open('data.txt', 'a') as outfile:
            json.dump(species, outfile)