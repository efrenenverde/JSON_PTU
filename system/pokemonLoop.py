import json
from models import capabilities
from models import baseStats
from models import speciesSkills
from models import evolution

SpecialNames = ['TYPE:', 'GIRATINA', 'MR.', 'MIME', 'HOOPA', 'TAPU', 'ZYGARDE', 'MELOETTA', 'KYUREM', 'TORNADUS', 'LANDORUS',
                'THUNDURUS', 'SHAYMIN', 'ROTOM', 'DEOXYS', 'WORMADAM', 'DARMANITAN', 'LYCANROC', 'WISHIWASHI', 'MINIOR', 'NECROZMA', 'NIDORAN',
                'MEOWSTIC', 'ZACIAN', 'ZAMAZENTA', 'INDEEDEE', 'EISCUE']
RegionalForms = ['RATTATA', 'RATICATE', 'RAICHU', 'SANDSHREW', 'SANDSLASH', 'VULPIX', 'NINETALES', 'DIGLETT', 'DUGTRIO', 'MEOWTH',
                 'PERSIAN', 'GEODUDE', 'GRAVELER', 'GOLEM', 'GRIMER', 'MUK', 'EXEGGUTOR', 'MAROWAK', 'PONYTA', 'RAPIDASH', 'SLOWPOKE', 'WEEZING',
                 'CORSOLA', 'ZIGZAGOON', 'LINOONE', 'DARUMAKA', 'YAMASK', 'STUNFISK']
RegionNames = ['Alola', 'Galar']
AbilityBreakers = ['Basic', 'Adv', 'High', 'Evolution:', 'Capability']
ExtraSpecialNames = ['MR.-MIME', 'DARMANITAN-Galar,']
NonOtherCapabilities = ['Overland', 'Sky', 'Swim',
                        'Levitate', 'Burrow', 'Jump', 'Power', 'Naturewalk']
Naturewalks = ['Grassland', 'Desert', 'Forest', 'Urban',
               'Wetlands', 'Cave', 'Ocean', 'Mountain', 'Tundra']
SpeciesWithWeirdStats = ['PUMPKABOO', 'GOURGEIST']
SkillNames = ['Athl', 'Acro', 'Combat', 'Stealth', 'Percep', 'Focus']


class PokemonLoop:
    SpeciesName = ''
    InfoArray = []
    Type = []
    Basic = []
    Advanced = []
    High = []
    BaseStats = baseStats.BaseStats()
    CapaList = capabilities.Capabilities()
    SpeciesSkills = speciesSkills.SpeciesSkills()
    Evolution = []
    HeightNum = 0
    HeightClass = ''
    WeightNum = 0

    def __init__(self, Data):
        if Data[0] not in SpecialNames:
            self.SpeciesName = Data[0]
        elif Data[0] == "JR.":
            self.SpeciesName = "MIME-JR."
        else:
            self.SpeciesName = Data[0] + '-' + Data[1]

        if self.SpeciesName in ExtraSpecialNames and Data[2] in RegionNames:
            self.SpeciesName += '-' + Data[2]
        elif self.SpeciesName in ExtraSpecialNames and self.SpeciesName.find(',') > 0:
            self.SpeciesName = self.SpeciesName.replace(
                ',', '') + '-' + Data[2]
        elif self.SpeciesName in RegionalForms and Data[1] in RegionNames:
            self.SpeciesName += '-' + Data[1]

        self.InfoArray = Data

    def resetAll(self):
        self.BaseStats = baseStats.BaseStats()
        self.Type = []
        self.Basic = []
        self.Advanced = []
        self.High = []
        self.CapaList = capabilities.Capabilities()
        self.SpeciesSkills = speciesSkills.SpeciesSkills()
        self.Evolution = []
        self.HeightNum = 0
        self.HeightClass = ''
        self.WeightNum = 0

    def setAll(self):
        self.setBaseStats()
        self.setBasicInformation()
        self.setCapabilities()
        self.setSkillList()
        self.setSizeBreedingDiet()

    # TODO: Review Evolution structure
    # TODO: Fix names with multiple words
    def setBasicInformation(self):
        i = 0
        while self.InfoArray[i] != "Basic" and self.InfoArray[i+1] != "Information":
            i += 1

        while self.InfoArray[i] != "Evolution:" and self.SpeciesName != "ROTOM-Appliance":
            if self.InfoArray[i] == "Type:":
                self.Type.append(self.InfoArray[i+1])
                if self.InfoArray[i+2] == '/':
                    self.Type.append(self.InfoArray[i+3])

            if self.InfoArray[i] == "Basic" and self.InfoArray[i+1] == "Ability":
                fullAbilityName = self.InfoArray[i+3]
                j = 1
                while self.InfoArray[i+3+j] not in AbilityBreakers:
                    fullAbilityName += ' ' + self.InfoArray[i+3+j]
                    j += 1
                self.Basic.append(fullAbilityName)

            if self.InfoArray[i] == "Adv" and self.InfoArray[i+1] == "Ability":
                fullAbilityName = self.InfoArray[i+3]
                j = 1
                while self.InfoArray[i+3+j] not in AbilityBreakers:
                    fullAbilityName += ' ' + self.InfoArray[i+3+j]
                    j += 1
                self.Advanced.append(fullAbilityName)

            if self.InfoArray[i] == "High" and (self.InfoArray[i+1] == "Ability" or self.InfoArray[i+1] == "Ability:"):
                j = 1
                if self.InfoArray[i+2] == "1:" or self.InfoArray[i+2] == "2:" or self.InfoArray[i+2] == "3:":
                    fullAbilityName = self.InfoArray[i+3]
                    while self.InfoArray[i+3+j] not in AbilityBreakers:
                        fullAbilityName += ' ' + self.InfoArray[i+3+j]
                        j += 1
                    self.High.append(fullAbilityName)
                else:
                    fullAbilityName = self.InfoArray[i+2]
                    while self.InfoArray[i+2+j] not in AbilityBreakers:
                        fullAbilityName += ' ' + self.InfoArray[i+2+j]
                        j += 1
                    self.High.append(fullAbilityName)
            i += 1
        while self.InfoArray[i] != "Size" and self.SpeciesName != "ROTOM-Appliance":
            if self.InfoArray[i] == "1" or self.InfoArray[i] == "2" or self.InfoArray[i] == "3":
                evolutionEntry = evolution.Evolution()
                evolutionEntry.Stage = int(self.InfoArray[i])
                evolutionEntry.Name = self.InfoArray[i+2]
                if evolutionEntry.Name.upper() in SpecialNames:
                    evolutionEntry.Name += ' ' + self.InfoArray[i+3]
                    i+=1
                if self.InfoArray[i+3] == "Minimum":
                    if self.InfoArray[i+4].find(',') > 0 or self.InfoArray[i+4].find(';') > 0:
                        evolutionEntry.MinLevel = int(self.InfoArray[i+4][:-1])
                        evolutionEntry.Extras = self.InfoArray[i+5]
                    else:
                        evolutionEntry.MinLevel = int(self.InfoArray[i+4])
                self.Evolution.append(evolutionEntry.toArray())
                i+=1
            else:
                i+=1
                
    def setBaseStats(self):
        if self.SpeciesName in SpeciesWithWeirdStats:
            return

        i = 0
        while self.InfoArray[i] != "Base" and self.InfoArray[i+1] != "Stats:":
            i += 1
        while self.InfoArray[i] != "Basic":
            if self.InfoArray[i] == "HP:":
                self.BaseStats.HIT = int(self.InfoArray[i+1])
                self.BaseStats.ATK = int(self.InfoArray[i+3])
                self.BaseStats.DEF = int(self.InfoArray[i+5])
                self.BaseStats.SAT = int(self.InfoArray[i+8])
                self.BaseStats.SDE = int(self.InfoArray[i+11])
                self.BaseStats.SPD = int(self.InfoArray[i+13])
                i += 13
            else:
                i += 1

    # TODO: Fix this mess
    def setCapabilities(self):
        i = 0
        foundCapabilities = False
        while i < len(self.InfoArray):
            if self.InfoArray[i] == "Capability":
                i += 2
                foundCapabilities = True

            if foundCapabilities:
                if self.InfoArray[i] == 'Overland':
                    self.CapaList.Overland = int(self.InfoArray[i+1][:-1])
                elif self.InfoArray[i] == "Sky":
                    if self.InfoArray[i+1] == "Forme,":
                        print('Shaymin please stop breaking my code')
                    elif self.InfoArray[i+1].find(',') > -1:
                        self.CapaList.Sky = int(
                            self.InfoArray[i+1][self.InfoArray[i+1].find(',')-1])
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
                        self.CapaList.Naturewalk.append(
                            self.InfoArray[i+1][1:self.InfoArray[i+j].find(')')])
                    else:
                        self.CapaList.Naturewalk.append(
                            self.InfoArray[i+1][1:self.InfoArray[i+j].find(')')])
                        while doneNaturewalk == False:
                            j += 1
                            self.CapaList.Naturewalk.append(
                                self.InfoArray[i+j][:self.InfoArray[i+j].find(')')])
                            doneNaturewalk = self.InfoArray[i+j].find(')') > 0
                elif self.InfoArray[i] == "Skill":
                    break
                elif self.InfoArray[i] not in NonOtherCapabilities and (len(self.InfoArray[i]) > 4 or self.InfoArray[i] == "Dead"):
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

    def extractSkillInfo(self, targetString):
        dice = 2
        mod = 0
        dice = int(targetString[0])
        if targetString.find('+') > 0:
            mod = int(targetString[targetString.find('+')+1])
        return [dice, mod]

    def setSizeBreedingDiet(self):
        i = 0

        if self.SpeciesName == "ROTOM-Appliance":
            return

        while self.InfoArray[i] != 'Height:':
            i += 1

        if self.SpeciesName in SpeciesWithWeirdStats:
            return

        try:
            self.HeightNum = float(self.InfoArray[i+4][:-1])
            self.HeightClass = self.InfoArray[i+5][1:-1]
        except:
            print(self.SpeciesName + ' messed up the size part')
            print('Info: ' + str(self.InfoArray[i:i+13]) )

        try:
            while self.InfoArray[i] != 'Weight:':
                i += 1
        
            self.CapaList.WeightClass = self.InfoArray[i+5][1:-1]
            self.WeightNum = float(self.InfoArray[i+4][:-2])
        except:
            print(self.SpeciesName + ' messed up the weight part')
            print('Info: ' + str(self.InfoArray[i:i+13]) )

    def setSkillList(self):
        i = 0
        while self.InfoArray[i] != 'Athl':
            i += 1

        if self.SpeciesName == "ALTARIA":
            self.SpeciesSkills.Athletics.Dice = 4
            self.SpeciesSkills.Athletics.Mod = 2

            self.SpeciesSkills.Acrobatics.Dice = 5
            self.SpeciesSkills.Acrobatics.Mod = 3

            self.SpeciesSkills.Combat.Dice = 1
            self.SpeciesSkills.Combat.Mod = 0

            self.SpeciesSkills.Stealth.Dice = 2
            self.SpeciesSkills.Stealth.Mod = 1

            self.SpeciesSkills.Perception.Dice = 4
            self.SpeciesSkills.Perception.Mod = 1

            self.SpeciesSkills.Focus.Dice = 3
            self.SpeciesSkills.Focus.Mod = 1
        else:
            self.SpeciesSkills.Athletics.Dice = self.extractSkillInfo(
                self.InfoArray[i+1])[0]
            self.SpeciesSkills.Athletics.Mod = self.extractSkillInfo(
                self.InfoArray[i+1])[1]

            self.SpeciesSkills.Acrobatics.Dice = self.extractSkillInfo(
                self.InfoArray[i+3])[0]
            self.SpeciesSkills.Acrobatics.Mod = self.extractSkillInfo(
                self.InfoArray[i+3])[1]

            self.SpeciesSkills.Combat.Dice = self.extractSkillInfo(
                self.InfoArray[i+5])[0]
            self.SpeciesSkills.Combat.Mod = self.extractSkillInfo(
                self.InfoArray[i+5])[1]

            self.SpeciesSkills.Stealth.Dice = self.extractSkillInfo(
                self.InfoArray[i+7])[0]
            self.SpeciesSkills.Stealth.Mod = self.extractSkillInfo(
                self.InfoArray[i+7])[1]

            self.SpeciesSkills.Perception.Dice = self.extractSkillInfo(
                self.InfoArray[i+9])[0]
            self.SpeciesSkills.Perception.Mod = self.extractSkillInfo(
                self.InfoArray[i+9])[1]

            self.SpeciesSkills.Focus.Dice = self.extractSkillInfo(
                self.InfoArray[i+11])[0]
            self.SpeciesSkills.Focus.Mod = self.extractSkillInfo(
                self.InfoArray[i+11])[1]

    def toJson(self):
        species = {}

        Abilities = {}
        Abilities['Basic'] = self.Basic
        Abilities['Advanced'] = self.Advanced
        Abilities['High'] = self.High

        species = []
        species.append({
            '_id': self.SpeciesName,
            'Base Stats': self.BaseStats.declareJson(),
            'Abilities': Abilities,
            'Evolution': self.Evolution,
            'Height': self.HeightNum,
            'Size Class': self.HeightClass,
            'Weight': self.WeightNum,
            'Capabilities': self.CapaList.declareJson(),
            'Skills': self.SpeciesSkills.declareJson()
        })

        with open('data.txt', 'a') as outfile:
            json.dump(species, outfile)
