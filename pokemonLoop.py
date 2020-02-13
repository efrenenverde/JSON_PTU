import json
from models import capabilities

class PokemonLoop:
    SpeciesName = ''
    InfoArray = []
    SpecialNames = ['TYPE:', 'GIRATINA', 'MR.', 'MIME', 'HOOPA', 'TAPU', 'ZYGARDE', 'MELOETTA', 'KYUREM', 'TORNADUS', 'LANDORUS', 'THUNDURUS',
    'SHAYMIN', 'ROTOM', 'DEOXYS', 'WORMADAM', 'DARMANITAN', 'LYCANROC', 'WISHIWASHI', 'MINIOR', 'NECROZMA']
    # TODO: Implement this on setCapabilities
    NonOtherCapabilities = ['Overland', 'Sky', 'Swim', 'Levitate', 'Burrow', 'Jump', 'Power', 'Naturewalk']
    CapaList = capabilities.Capabilities

    def __init__(self, Data):
        if Data[0] not in self.SpecialNames:
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
         #       i+=2
                foundCapabilities = True

            if foundCapabilities:
                if self.InfoArray[i] == 'Overland':
                    self.CapaList.Overland = int(self.InfoArray[i+1][:-1])
          #          i += 1
                elif self.InfoArray[i] == "Sky":
                    if self.InfoArray[i+1] == "Forme,":
                        print('Shaymin please stop breaking my code please')
           #             i += 1
                    elif self.InfoArray[i+1].find(',') > -1:
                        self.CapaList.Sky = int(self.InfoArray[i+1][self.InfoArray[i+1].find(',')-1])
            #            i += 1
                    else:
                        self.CapaList.Sky = int(self.InfoArray[i+1])
             #           i += 1
                elif self.InfoArray[i] == "Swim":
                    self.CapaList.Swim = int(self.InfoArray[i+1][:-1])
              #      i += 1
                elif self.InfoArray[i] == "Levitate":
                    self.CapaList.Levitate = int(self.InfoArray[i+1][:-1])
               #     i += 1
                elif self.InfoArray[i] == "Burrow":
                    self.CapaList.Burrow = int(self.InfoArray[i+1][:-1])
                #    i += 1
                elif self.InfoArray[i] == "Jump":
                    self.CapaList.JumpH = int(self.InfoArray[i+1][0])
                    self.CapaList.JumpL = int(self.InfoArray[i+1][-2])
                 #   i += 1
                elif self.InfoArray[i] == "Power":
                    if self.InfoArray[i+1].find(',') > -1:
                        self.CapaList.Power = int(self.InfoArray[i+1][:-1])
                  #      i += 1
                    else:
                        self.CapaList.Power = int(self.InfoArray[i+1])
                   #     i += 1                
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

            i += 1
        print(self.SpeciesName, self.CapaList.__dict__)


    def toArray(self):
        species = {}
        species[self.SpeciesName] = []
        species[self.SpeciesName].append({
            '_id': self.SpeciesName
        })


data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)