


def damage(character, enemy):
    if enemy_defending == True:
        Damage = character.attack - (enemy.defense * 1.2)
    else:
        Damage = character.attack - (enemy.defense * 0.8)
        

    return Damage


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