class SkillTemplate:
    Dice = 2,
    Mod = 0

    def __init__(self, DiceValue, ModValue):
        self.reset(DiceValue, ModValue)
    
    def reset(self, DiceValue, ModValue):
        self.Dice = DiceValue
        self.ModValue = ModValue

class SpeciesSkills:
    Acrobatics = SkillTemplate(2, 0)
    Athletics = SkillTemplate(2, 0)
    Combat = SkillTemplate(2, 0)
    Stealth = SkillTemplate(2, 0)
    Perception = SkillTemplate(2, 0)
    Focus = SkillTemplate(2, 0)

    def __init__(self):
        self.reset()

    def reset(self):
        self.Acrobatics = SkillTemplate(2, 0)
        self.Athletics = SkillTemplate(2, 0)
        self.Combat = SkillTemplate(2, 0)
        self.Stealth = SkillTemplate(2, 0)
        self.Perception = SkillTemplate(2, 0)
        self.Focus = SkillTemplate(2, 0)
    
    def declareJson(self):
        Athletics = {}
        Athletics['Dice'] = self.Athletics.Dice
        Athletics['Mod'] = self.Athletics.Mod

        Acrobatics = {}
        Acrobatics['Dice'] = self.Acrobatics.Dice
        Acrobatics['Mod'] = self.Acrobatics.Mod

        Combat = {}
        Combat['Dice'] = self.Combat.Dice
        Combat['Mod'] = self.Combat.Mod

        Stealth = {}
        Stealth['Dice'] = self.Stealth.Dice
        Stealth['Mod'] = self.Stealth.Mod

        Perception = {}
        Perception['Dice'] = self.Perception.Dice
        Perception['Mod'] = self.Perception.Mod

        Focus = {}
        Focus['Dice'] = self.Focus.Dice
        Focus['Mod'] = self.Focus.Mod

        Skills = {}
        Skills['Athletics'] = Athletics
        Skills['Acrobatics'] = Acrobatics
        Skills['Combat'] = Combat
        Skills['Stealth'] = Stealth
        Skills['Perception'] = Perception
        Skills['Focus'] = Focus

        return Skills