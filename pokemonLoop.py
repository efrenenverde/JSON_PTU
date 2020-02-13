import json
from models import capabilities

SpecialNames = ['TYPE:', 'GIRATINA', 'MR.', 'MIME', 'HOOPA', 'TAPU', 'ZYGARDE', 'MELOETTA', 'KYUREM', 'TORNADUS', 'LANDORUS', 'THUNDURUS',
    'SHAYMIN', 'ROTOM', 'DEOXYS', 'WORMADAM', 'DARMANITAN', 'LYCANROC', 'WISHIWASHI', 'MINIOR', 'NECROZMA']
NonOtherCapabilities = ['Overland', 'Sky', 'Swim', 'Levitate', 'Burrow', 'Jump', 'Power', 'Naturewalk']
Naturewalks = ['Grassland', 'Desert', 'Forest', 'Urban', 'Wetlands', 'Cave', 'Ocean', 'Mountain', 'Tundra']

class PokemonLoop:
    SpeciesName = ''
    InfoArray = []
    
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
        self.setCapabilities()
            
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
                    print(self.SpeciesName, self.CapaList.__dict__)
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

    def toArray(self):
        species = {}

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
            'Capabilities': Capabilities
        })

        with open('data.txt', 'a') as outfile:
            json.dump(species, outfile)