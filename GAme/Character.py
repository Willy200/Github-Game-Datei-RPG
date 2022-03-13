class Character:
    Player_Skill_Points = 20 #Anfangswert den man auszugeben hat
    def __init__(self):
        pass # lass es so einfach

    def Stats(self, health, attack, defense, special, initiative, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special = special
        self.init = initiative
        self.name = name
        self.level = 0

    def Battle_Stats(self): # die Brauchen wir, weil während des Kampfs sich die Statistiken ändern werden z.B. Health und wir wollen nicht, dass es permament reduziert bleibt
        self.Battle_Health_Max = self.health
        self.Battle_Health_Actual = self.health
        self.Battle_Attack_Max = self.attack
        self.Battle_Attack_Actual = self.attack
        self.Battle_Defense_Max = self.defense
        self.Battle_Defense_Actual = self.defense
        self.Battle_Special_Max = self.special
        self.Battle_Special_Actual = self.special
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
        Surface = pygame.Surface((100,200))
        surface.fill("Red")
        screen.blit(surface,(400,200))
        text = font.render("Player1",False,"Black")


class Item:
    def __init__(self):
        pass
    def ItemDescritpion(self, name, description):
        self.ItemDescription = description
        self.name = name
    def ItemAttributes(self, Attack_Modifier, Defense_Modifier, Special_Modifier, Health_Modifier):
        self.AttMod = Attack_Modifier
        self.DefMod = Defense_Modifier
        self.SpecMod = Special_Modifier
        self.HeaMod = Health_Modifier
    def Modify(self, character):
        character.Battle_Attack_Actual = character.Battle_Attack_Actual * self.AttMod
        character.Battle_Defense_Actual = character.Battle_Defense_Actual * self.DefMod
        character.Battle_Special_Actual = character.Battle_Special_Actual * self.SpecMod
        character.Battle_Health_Actual = character.Battle_Health_Actual * self.HeaMod
    def Unequip(self, character):
        character.Battle_Attack_Actual = character.attack
        character.Battle_Defense_Actual = character.defense
        character.Battle_Special_Actual = character.special
        character.Battle_Health_Actual = character.health

#class Player(Character): < hier unsicher ob wir es brauchen an zwei Unterklassen zu teilen
#class Enemy(Character):
#Boy = Character()
#Boy.Stats(15, 5,5,10,"ku")
#Boy.setHealth(int(input()))
#print(Boy.health)

#Magic_Wand = Item()
#Magic_Wand.ItemDescritpion("Magic Wand", "It is a magic wand, it increases the special damage")
#Magic_Wand.ItemAttributes(1, 1, 1.2, 1)



