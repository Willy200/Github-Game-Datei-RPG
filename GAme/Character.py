class Character:

    def __init__(self):
        self.isDefending = False
        self.coins = 0

    def stats(self, health, attack, defense, special, initiative, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special = special
        self.init = initiative
        self.name = name

    def Battle_Stats(self):  # die Brauchen wir, weil während des Kampfs sich die Statistiken ändern werden z.B. Health und wir wollen nicht, dass es permament reduziert bleibt
        self.Battle_Health_Max = self.health * 5
        self.Battle_Health_Actual = self.health * 5
        self.Battle_Attack_Max = self.attack * 2
        self.Battle_Attack_Actual = self.attack * 2
        self.Battle_Defense_Max = self.defense * 2
        self.Battle_Defense_Actual = self.defense * 2
        self.Battle_Special_Max = self.special * 4
        self.Battle_Special_Actual = self.special * 4
        self.Battle_Initiative_Actual = self.init
        self.Battlle_Initiative_Max = self.init

    def setHealth(self, amount):
        self.Battle_Health_Actual = self.Battle_Health_Actual + amount

    def getHealth(self):
        return self.health

    def setAttack(self, amount):
        self.Battle_Attack_Actual = self.Battle_Attack_Actual * amount

    def getAttack(self):
        return self.attack

    def setDefense(self, amount):
        self.Battle_Defense_Actual = self.Battle_Defense_Actual * amount

    def getDefense(self):
        return self.defense

    def setSpecial(self, amount):
        self.Battle_Special_Actual = self.Battle_Special_Actual + amount
        if self.Battle_Special_Actual > self.Battle_Special_Max:
            self.Battle_Special_Actual = self.Battle_Special_Max

    def getSpecial(self):
        return self.special

    def RestoreStats(self):
        self.Battle_Health_Actual = self.Battle_Health_Max
        self.Battle_Attack_Actual = self.Battle_Attack_Max
        self.Battle_Defense_Actual = self.Battle_Defense_Max
        self.Battle_Special_Actual = self.Battle_Special_Max
        self.Battle_Initiative_Actual = self.Battlle_Initiative_Max

    def Character_Darstellen(self):
        Surface = pygame.Surface((100, 200))
        surface.fill("Red")
        screen.blit(surface, (400, 200))
        text = font.render("Player1", False, "Black")

    def Defend(self):
        self.isDefending = True

        return self.isDefending

    def NoDefend(self):
        self.isDefending = False
        return self.isDefending


class Item:
    def __init__(self):
        pass

    def ItemDescritpion(self, name, description):
        self.ItemDescription = description
        self.name = name

    def ItemAttributes(self, Attack_Modifier, Defense_Modifier, Special_Modifier, Health_Modifier, Initiative_Modifier):
        self.AttMod = Attack_Modifier
        self.DefMod = Defense_Modifier
        self.SpecMod = Special_Modifier
        self.HeaMod = Health_Modifier
        self.InitMod = Initiative_Modifier

    def Modify(self, character):
        character.Battle_Attack_Max = character.Battle_Attack_Max * self.AttMod
        character.Battle_Defense_Max = character.Battle_Defense_Max * self.DefMod
        character.Battle_Special_Max = character.Battle_Special_Max * self.SpecMod
        character.Battle_Health_Max = character.Battle_Health_Max * self.HeaMod
        character.Battle_Initiative_Max = character.Battle_Initiative_Max * self.InitMod

    def Unequip(self, character):
        character.Battle_Attack_Max = character.attack
        character.Battle_Defense_Max = character.defense
        character.Battle_Special_Max = character.special
        character.Battle_Health_Max = character.health