import json
import os
from models import capabilities
from models import baseStats
from models import speciesSkills
from models import evolution
import numberClear

fetchNumber = numberClear.getNumberDictionary()

SpecialNames = ['TYPE:', 'GIRATINA', 'MR.', 'MIME', 'HOOPA', 'TAPU', 'ZYGARDE', 'MELOETTA', 'KYUREM', 'TORNADUS', 'LANDORUS',
                'THUNDURUS', 'SHAYMIN', 'ROTOM', 'DEOXYS', 'WORMADAM', 'DARMANITAN', 'LYCANROC', 'WISHIWASHI', 'MINIOR', 'NECROZMA', 'NIDORAN',
                'MEOWSTIC', 'ZACIAN', 'ZAMAZENTA', 'INDEEDEE', 'EISCUE', 'URSHIFU']
RegionalForms = ['RATTATA', 'RATICATE', 'RAICHU', 'SANDSHREW', 'SANDSLASH', 'VULPIX', 'NINETALES', 'DIGLETT', 'DUGTRIO', 'MEOWTH',
                 'PERSIAN', 'GEODUDE', 'GRAVELER', 'GOLEM', 'GRIMER', 'MUK', 'EXEGGUTOR', 'MAROWAK', 'PONYTA', 'RAPIDASH', 'SLOWPOKE', 'WEEZING',
                 'CORSOLA', 'ZIGZAGOON', 'LINOONE', 'DARUMAKA', 'YAMASK', 'STUNFISK', 'FARFETCHD', 'SLOWBRO']
RegionNames = ['Alola', 'Galar']
AbilityBreakers = ['Basic', 'Adv', 'High', 'Evolution:', 'Capability']
ExtraSpecialNames = ['MR.-MIME', 'DARMANITAN-Galar,']
NonOtherCapabilities = ['Overland', 'Sky', 'Swim',
                        'Levitate', 'Burrow', 'Jump', 'Power', 'Naturewalk']
Naturewalks = ['Grassland', 'Desert', 'Forest', 'Urban',
               'Wetlands', 'Cave', 'Ocean', 'Mountain', 'Tundra']
SpeciesWithWeirdStats = ['PUMPKABOO', 'GOURGEIST']
SkillNames = ['Athl', 'Acro', 'Combat', 'Stealth', 'Percep', 'Focus']
MoveListBreakers = ['TM', 'Type:', 'Tutor', 'Egg', 'Basic', 'MegaEvolution']
PokemonWithNoTMList = ['ROTOM-Appliance', 'CATERPIE', 'METAPOD','WEEDLE', 'KAKUNA', 'MAGIKARP', 'WURMPLE', 'SILCOON', 'CASCOON', 'SCATTERBUG',
 'KRICKETOT', 'COMBEE', 'SMEARGLE', 'DITTO', 'BELDUM', 'COSMOG', 'COSMOEM', 'SPEWPA']
GenderRatioNull = ['No', 'Hermaphrodite', 'Genderless']


class PokemonLoop:
    SpeciesName = ''
    DexNumber = 0
    PTUNumber = 0
    InfoArray = []
    Type = []
    Basic = []
    Advanced = []
    High = []
    BaseStats = baseStats.BaseStats()
    CapaList = capabilities.Capabilities()
    GenderRatio = 0
    EggGroup = []
    AvgHatch = -1
    Diet = []
    Habitat = []
    SpeciesSkills = speciesSkills.SpeciesSkills()
    Evolution = []
    HeightNum = 0
    HeightClass = ''
    WeightNum = 0
    LevelUpMoveList = []
    TMMoveList = []
    EggMoveList = []
    TutorMoveList = []

    def __init__(self, Data, currNumber):
        self.PTUNumber = currNumber
        if Data[0] not in SpecialNames:
            self.SpeciesName = Data[0]
            if "JR" in Data[0]:
                self.SpeciesName = 'MIME-JR.'
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
        self.DexNumber = 0
        self.Type = []
        self.Basic = []
        self.Advanced = []
        self.High = []
        self.CapaList = capabilities.Capabilities()
        self.SpeciesSkills = speciesSkills.SpeciesSkills()
        self.Evolution = []
        self.GenderRatio = 0
        self.EggGroup = []
        self.AvgHatch = -1
        self.Diet = []
        self.Habitat = []
        self.HeightNum = 0
        self.HeightClass = ''
        self.WeightNum = 0
        self.LevelUpMoveList = []
        self.TMMoveList = []
        self.EggMoveList = []
        self.TutorMoveList = []

    def setAll(self):

        self.setBaseStats()
        self.setBasicInformation()
        self.setCapabilities()
        self.setSkillList()
        self.setSize()
        self.setSize()
        self.setLevelUpList()
        self.setTMList()
        self.setEggMoveList()
        self.setTutorMoveList()
        self.setGenderRatio()
        self.setEggGroup()
        self.setHatchRate()
        self.setDiet()
        self.setHabitat()
        self.setTypes()
        self.setDexNumber()

    def setTypes(self):
        i = 0
        self.Type = []

        while self.InfoArray[i] != "Type:":
            if i > len(self.InfoArray)-5:
                print(self.SpeciesName + " no Type: found")
                return
            i += 1

        self.Type.append(self.InfoArray[i+1])

        if self.InfoArray[i+2] == "/":
            self.Type.append(self.InfoArray[i+3])
        else:
            self.Type.append("null")

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
                else:
                    self.Type.append('Null')

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
                elif (self.InfoArray[i+3] == "(A)" or self.InfoArray[i+3] == "(G)") and self.InfoArray[i+4] == "Minimum":
                    if self.InfoArray[i+5].find(',') > 0 or self.InfoArray[i+5].find(';') > 0:
                        evolutionEntry.MinLevel = int(self.InfoArray[i+5][:-1])
                        evolutionEntry.Extras = self.InfoArray[i+6]
                    else:
                        evolutionEntry.MinLevel = int(self.InfoArray[i+5])
                self.Evolution.append(evolutionEntry.toArray())
                i += 1
            else:
                i += 1

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
                            self.InfoArray[i+1][0:-1])
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

    def setSize(self):
        i = 0

        if self.SpeciesName == "ROTOM-Appliance" or self.SpeciesName in SpeciesWithWeirdStats:
            return

        while self.InfoArray[i] != 'Height:':
            i += 1

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

    def setGenderRatio(self):
        i = 0

        if self.SpeciesName == "ROTOM-Appliance":
            return

        while self.InfoArray[i] != "Ratio:":
            if i > len(self.InfoArray)-5:
                return
            i += 1

        if self.InfoArray[i+1] in GenderRatioNull:
            self.GenderRatio = -1
        else:
            self.GenderRatio = float(self.InfoArray[i+1][:-1])

    def setEggGroup(self):
        i = 0

        while self.InfoArray[i] != "Group:":
            if i > len(self.InfoArray)-5:
                print(self.SpeciesName + " Group: not found")
                return
            i += 1

        self.EggGroup.append(self.InfoArray[i+1])

        if self.EggGroup[0] == "Water":
            self.EggGroup[0] = "Water " + self.InfoArray[i+2]
            i += 1
        
        if self.InfoArray[i+2] == "/":
            self.EggGroup.append(self.InfoArray[i+3])
            if self.EggGroup[1] == "Water":
                self.EggGroup[1] = "Water " + self.InfoArray[i+4]
                i += 1

    def setHatchRate(self):
        i = 0

        while self.InfoArray[i] != "Rate:":
            if i > len(self.InfoArray)-5:
                return
            i += 1
        
        self.AvgHatch = int(self.InfoArray[i+1])

    def setDiet(self):
        i = 0

        while self.InfoArray[i] != "Diet:":
            if i > len(self.InfoArray)-5:
                print(self.SpeciesName + " no Diet: found")
                return
            i += 1

        self.Diet.append(self.InfoArray[i+1])

        while ',' in self.InfoArray[i+1]:
            i+=1
            j = 0
            self.Diet[j] = self.Diet[j][:-1]
            self.Diet.append(self.InfoArray[i+1])

    def setHabitat(self):
        i = 0

        while self.InfoArray[i] != "Habitat:":
            if i > len(self.InfoArray)-2:
                print(self.SpeciesName + " no Habitat: found")
                return
            i += 1

        self.Habitat.append(self.InfoArray[i+1])

        while ',' in self.InfoArray[i+1]:
            i += 1
            j = 0
            self.Habitat[j] = self.Habitat[j][:-1]
            self.Habitat.append(self.InfoArray[i+1])

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

    def setLevelUpList(self):
        i = 0

        if self.SpeciesName == "ROTOM-Appliance":
            return

        while self.InfoArray[i] != "Level" and self.InfoArray[i+1] != "Up":
            i += 1

        # Positioned on -Level- Up Move List, next line puts us on
        i += 4

        while self.InfoArray[i] not in MoveListBreakers:
            try:
                level = int(self.InfoArray[i])
            except:
                level = "Evo"
            i += 1
            fullName = ''
            while self.InfoArray[i] != '-':
                fullName += self.InfoArray[i]
                if self.InfoArray[i+1] != '-':
                    fullName += ' '
                i += 1

            self.LevelUpMoveList.append({
                "Level": level,
                "Move": fullName
            })

            i += 2

    def setTMList(self):
        i = 0

        if self.SpeciesName in PokemonWithNoTMList:
            return

        while self.InfoArray[i] != "TM":
            i += 1

        # Positioned on -TM- Move List
        i += 3

        while self.InfoArray[i] not in MoveListBreakers:
            level = self.InfoArray[i]
            self.TMMoveList.append(level)

            while "," not in self.InfoArray[i]:
                if self.InfoArray[i] not in MoveListBreakers:
                    i += 1
                else:
                    return
            
            i+=1

    def setEggMoveList(self):
        i = 0

        while self.InfoArray[i]+self.InfoArray[i+1] != "EggMove":
            if i > len(self.InfoArray)-5:
                return
            i += 1

        # Positioned on -Egg- Move List
        i += 3

        while self.InfoArray[i] not in MoveListBreakers and i < len(self.InfoArray):
            egg = self.InfoArray[i]
            
            if self.InfoArray[i+1] in MoveListBreakers:
                self.EggMoveList.append(egg)
                return

            if "," not in egg:
                while "," not in egg:
                    i += 1
                    if self.InfoArray[i] not in MoveListBreakers and i < len(self.InfoArray):
                        if self.InfoArray[i+1] in MoveListBreakers:
                            egg += " " + self.InfoArray[i]
                            self.EggMoveList.append(egg)
                            return
                        egg += " " + self.InfoArray[i]
                    else:
                        return
            
            self.EggMoveList.append(egg[:-1])
            i+=1

    def setTutorMoveList(self):
        i = 0
        while self.InfoArray[i]+self.InfoArray[i+1] != "TutorMove":
            if i > len(self.InfoArray)-5:
                return
            i += 1

        # Positioned on -Tutor- Move List
        i += 3

        while self.InfoArray[i] not in MoveListBreakers and i < len(self.InfoArray)-1:
            tutor = self.InfoArray[i]

            if self.InfoArray[i+1] in MoveListBreakers or i > len(self.InfoArray)-1 :
                self.TutorMoveList.append(tutor)
                return

            if "," not in tutor:
                while "," not in tutor:
                    i += 1
                    if self.InfoArray[i] not in MoveListBreakers and i < len(self.InfoArray)-1:
                        if self.InfoArray[i+1] in MoveListBreakers:
                            tutor += " " + self.InfoArray[i]
                            self.TutorMoveList.append(tutor)
                            return
                        tutor += " " + self.InfoArray[i]
                    else:
                        tutor += " " + self.InfoArray[i]
                        self.TutorMoveList.append(tutor)
                        return
            
            self.TutorMoveList.append(tutor[:-1])
            i+=1

        if i == len(self.InfoArray)-1:
            tutor = self.InfoArray[i]
            self.TutorMoveList.append(tutor)

    def setDexNumber(self):
        self.DexNumber = fetchNumber.getNumber(self.SpeciesName.upper())

    def toJson(self):

        if (self.SpeciesName == 'ROTOM-Appliance'):
            return

        if len(self.Evolution) < 1:
            print(self.SpeciesName + " tiene las evos mal")

        self.SpeciesName = self.SpeciesName.replace('Galar', 'Galarian')
        self.SpeciesName = self.SpeciesName.replace('Alola', 'Alolan')
        
        species = {}    

        Abilities = {}
        Abilities['Basic'] = self.Basic
        Abilities['Advanced'] = self.Advanced
        Abilities['High'] = self.High

        BreedingInfo = {}
        BreedingInfo['Gender Ratio'] = self.GenderRatio
        BreedingInfo['Egg Group'] = self.EggGroup
        BreedingInfo['Average Hatch Rate'] = self.AvgHatch
        
        species = []
        species.append({
            '_id': self.SpeciesName,
            'number': self.DexNumber,
            'ptuNumber': self.PTUNumber,
            'Base Stats': self.BaseStats.declareJson(),
            'Type': self.Type,
            'Abilities': Abilities,
            'Evolution': self.Evolution,
            'Height': self.HeightNum,
            'Size Class': self.HeightClass,
            'Weight': self.WeightNum,
            'Breeding Information': BreedingInfo,
            'Diet': self.Diet,
            'Habitat': self.Habitat,
            'Capabilities': self.CapaList.declareJson(),
            'Level Up Move List': self.LevelUpMoveList,
            'TM Move List': self.TMMoveList,
            'Egg Move List': self.EggMoveList,
            'Tutor Move List': self.TutorMoveList,
            'Skills': self.SpeciesSkills.declareJson()
        })

        specie = {
            '_id': self.SpeciesName,
            'number': self.DexNumber,
            'ptuNumber': self.PTUNumber,
            'BaseStats': self.BaseStats.declareJson(),
            'Type': self.Type,
            'Abilities': Abilities,
            'Evolution': self.Evolution,
            'Height': self.HeightNum,
            'SizeClass': self.HeightClass,
            'Weight': self.WeightNum,
            'BreedingInformation': BreedingInfo,
            'Diet': self.Diet,
            'Habitat': self.Habitat,
            'Capabilities': self.CapaList.declareJson(),
            'LevelUpMoveList': self.LevelUpMoveList,
            'TMMoveList': self.TMMoveList,
            'EggMoveList': self.EggMoveList,
            'TutorMoveList': self.TutorMoveList,
            'Skills': self.SpeciesSkills.declareJson()
        }

        with open('data.txt', 'a') as outfile:
            json.dump(species, outfile)

        speciesJson = 'species/' + self.SpeciesName + ".json"
        
        try:
            os.remove(speciesJson)
        except IOError:
            print('First save of ' + self.SpeciesName)

        with open(speciesJson, 'a') as outfile:
            json.dump(specie, outfile)
