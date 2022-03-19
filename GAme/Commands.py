


def damage(character, enemy):
    if enemy.isDefending:
        Damage = character.Battle_Attack_Actual - (enemy.Battle_Defense_Actual * 1.2)
        if Damage <= 1:
            Damage = 1
    else:
        Damage = character.Battle_Attack_Actual - (enemy.Battle_Defense_Actual * 0.8)
        if Damage <= 1:
            Damage = 1
    enemy.setHealth(-Damage)


def heal(character, amount):
    character.setHealth(amount)

def weaken(character, amount):
    character.setDefense(amount)

def Use_Special(character, amount):
    character.setSpecial(character, amount)

i = 0
T1 = "Welcome to the new Turnamento"
T2 = "These formidble Worriors will be your Opponent"
T3 = "Can you beat them all ? Will you be the new Champion? "
T4 = "We will know it soon!"


Text = [T1,T2,T2]

def darstellreihenfolge(Text):
    global i

    if Player_Input_SPACE == True:
        # Text[i] = Text[i+1]
        i += 1
    if Player_Input_ALT == True:
        # Text[i] = Text [i-1]
        i -= 1
    if i < 0:
        i = 0
    return i
"""def darstellreihenfolge (Text):
    if Player_Input_SPACE == True:
        Text [i] = Text[i+1]
    if Player_Input_ALT == True:
        Text [i] = Text [i-1]
    if i < 0:
        i = 0
    return Text[i]"""
#screen.blit(Text[i], (20, 40))