import pygame
from Character import Character
from sys import exit
from Commands import damage
from random import *
from Items import Magic_Wand
from Enemies import Enemy_Wizard, Enemy_Rogue, Enemy_Warrior

pygame.init()


class Buttons:
    def __init__(self, screen, color, XPos, YPos, XLen, YLen, Willyszahl, Text, TextColor, XPos_Text,
                 YPos_Text):  # Man kann die vorbestimmte Farben wie RED = (255, 0, 0) sowohl bei rect als
        # auch bei Text benutzen
        pygame.draw.rect(screen, color, [XPos, YPos, XLen, YLen], Willyszahl)
        Buttons_Text = font.render(Text, False, TextColor)
        screen.blit(Buttons_Text, (XPos_Text, YPos_Text))


class Bar:
    def __init__(self, screen, color, XPos, YPos, XLen, YLen, Border, Character_Stat, Character_Stat_Max, TextColor,
                 XPos_Text,
                 YPos_Text):
        pygame.draw.rect(screen, color, [XPos, YPos, XLen, YLen], Border)
        Buttons(screen, color, XPos, YPos, 200 * (Character_Stat / Character_Stat_Max), 20, 20,
                str((Character_Stat / Character_Stat_Max) * 100)[0:3] + "%", TextColor, XPos_Text, YPos_Text)


def UP_DOWN():
    global A
    global Stage1
    global Main_Menu
    global Player_Creation
    global B
    global Player_Input_DOWN
    global Player_Input_UP
    global Player_Input_LEFT
    global Player_Input_RIGHT

    if event.type == pygame.KEYDOWN and Stage1 == True:
        if Player_Input_UP:
            A -= 1
            Player_Input_UP = False
            if A == 0:
                A = 4
        elif Player_Input_DOWN:
            A += 1
            Player_Input_DOWN = False
            if A == 5:
                A = 1
    elif event.type == pygame.KEYDOWN and Main_Menu == True:
        if Player_Input_UP:
            A = 1
            Player_Input_UP = False
        elif Player_Input_DOWN:
            A = 0
            Player_Input_DOWN = False
    elif event.type == pygame.KEYDOWN and Player_Creation == True:
        if Player_Input_DOWN:
            A += 1
            Player_Input_DOWN = False
            if A == 6:
                A = 1
        if Player_Input_UP:
            A -= 1
            Player_Input_UP = False
            if A == 0:
                A = 5
        if Player_Input_LEFT:
            B -= 1
            Player_Input_LEFT = False
            if B == 0:
                B = 1
        if Player_Input_RIGHT:
            B += 1
            Player_Input_RIGHT = False
            if B == 3:
                B = 2
    elif Stage2 == True and Player_Input_UP:
        B -= 1
        Player_Input_UP = False
        if B == 0:
            B = 1
    elif Stage2 == True and Player_Input_DOWN == True:
        B += 1
        Player_Input_DOWN = False
        if B == 3:
            B = 2
    elif Rest_Phase == True:
        if Player_Input_DOWN:
            A -= 1
            Player_Input_DOWN = False
            if A == 0:
                A = 2
        if Player_Input_UP:
            A += 1
            Player_Input_UP = False
            if A == 3:
                A = 1
        if Player_Input_LEFT:
            B -= 1
            Player_Input_LEFT = False
            if B == 0:
                B = 1
        if Player_Input_RIGHT:
            B += 1
            Player_Input_RIGHT = False
            if B == 3:
                B = 2


def UP_DOWN_2():  # nicht beruhren, hab eine Idee
    global A
    global B
    global List_of_Buttons_X
    global List_of_Buttons_Y
    global Player_Input_DOWN
    global Player_Input_UP
    global Player_Input_LEFT
    global Player_Input_RIGHT

    if Player_Input_UP:
        A -= 1
        Player_Input_UP = False
        if A == -1:
            A = len(List_of_Buttons_Y) - 1
    if Player_Input_DOWN:
        A += 1
        Player_Input_DOWN = False
        if A == len(List_of_Buttons_Y):
            A = 0
    if Player_Input_RIGHT:
        B += 1
        Player_Input_RIGHT = False
        if B >= len(List_of_Buttons_X):
            B = 0
    if Player_Input_LEFT:
        B -= 1
        Player_Input_LEFT = False
        if B <= -1:
            B = len(List_of_Buttons_X) - 1


def SwitchTurns():
    global A
    global Stage1
    global Stage2
    global TurnOrder
    global Player_Input_SPACE
    A = 0
    Stage1 = True
    Stage2 = False
    if TurnOrder == 1:
        Enemy.NoDefend()
        TurnOrder = 2
    elif TurnOrder == 2:
        Player.NoDefend()
        TurnOrder = 1
    Player_Input_SPACE = False


screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Spiel")
Frames = pygame.time.Clock()
font = pygame.font.Font("Fonts/Pixeltype.ttf", 30)

################################### Variablen definiert, damit Global ###############################################
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Round_Counter = 1

A = 0  # Gibt die Stufe in Stage1 an die gerade ausgewählt und Angezeigt wird
B = 0  # Gibt die Stufe in Stage2 Attack_Untermenü an die gerade ausgewählt und Angezeigt wird
Shop = False
Enemy_view = False
TurnOrder = 1
Stat_Points = 2
Stats_Creation = [1, 1, 1, 1, 1]
Enemy_List = [Enemy_Rogue, Enemy_Wizard, Enemy_Warrior]
temp_round_att = 0
temp_round_def = 0
Rest_Phase = False
Player_Buff = False
Battle = False
Player_Creation = False
Player_Input_DOWN = False
Player_Input_UP = False
Player_Input_SPACE = False
Player_Input_ALT = False
Player_Input_RIGHT = False
Player_Input_LEFT = False
Stage1 = False
Stage2 = False
Main_Menu = True
List_of_Buttons_X = []
List_of_Buttons_Y = []
############################################################# Texturen########################################
Background = pygame.Surface((1000, 600))
surface3 = pygame.Surface((200, 50))
surface3.fill("Red")
Background.fill("White")
sky = pygame.image.load("Graphics/Sky.png")
ground = pygame.image.load("Graphics/ground.png")
Enemy_picture = pygame.image.load("Graphics/Gegner Skelet.png")
Player_picture = pygame.image.load("Graphics/character_1.png")
################################################################ Schrift ############################################
Attack_text = font.render("ATTACK", False, RED)
Attack_Add = font.render("+", False, "White")
Attack_Sub = font.render("-", False, "White")
Defense_text = font.render("Defense", False, "White")
Special_text = font.render("Special", False, "White")
Item_text = font.render("Item", False, "White")
Sword_text = font.render("Sword", False, "White")
Bow_text = font.render("Bow", False, "White")
Shield_text = font.render("Shield", False, "White")
Attck_Buff_text = font.render("Attack Buff", False, "White")
Defense_Buff_text = font.render("Defense Buff", False, "White")
Potion_Text = font.render("Potion", False, "White")
Round_Counter_description = font.render("Round Number:", False, "Black")
Magic_Wand_Description = font.render(str(Magic_Wand.ItemDescription), False, "White")
################################################################### Text darstellen ###################################
i = 0
T1 = font.render("Welcome to the new Turnamento", False, "Black")
T2 = font.render("These formidble Worriors will be your Opponent", False, "Black")
T3 = font.render("Can you beat them all ? Will you be the new Champion? ", False, "Black")
T4 = font.render(" ", False, "Black")
Text = [T1, T2, T3, T4]
# screen.blit(Text[i], (20, 40))
##################################################################### main Game loop ##################################
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # guckt ob exit gedückt wird(wichtig um Fenster zu schließen)

            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:  # Das alles hier guck ob eine Taste gedrückt wurde. Wenn sie
            # gedrückt wird ist die entsprechende Input Variable auf TRUE gesetzt, sonst nicht. Alle anderen sind False.
            match event.key:
                case pygame.K_RIGHT:
                    Player_Input_RIGHT = True
                case pygame.K_LEFT:
                    Player_Input_LEFT = True
                case pygame.K_UP:
                    Player_Input_UP = True
                case pygame.K_DOWN:
                    Player_Input_DOWN = True
                case pygame.K_SPACE:
                    Player_Input_SPACE = True
                case pygame.K_m:
                    Player_Input_ALT = True
        UP_DOWN_2()
    pygame.display.update()
    screen.blit(Background, (0, 0))

    ################### ERSTE MENÜ UND INPUT PHASE ##################################################################

    if Main_Menu:
        Start_Button = Buttons(screen, BLACK, 400, 200, 150, 75, 100, "Start", "White", 450, 220)
        Exit_Button = Buttons(screen, BLACK, 400, 300, 150, 75, 100, "Quit", "White", 450, 320)
        List_of_Buttons_X = [Start_Button]
        List_of_Buttons_Y = [Start_Button, Exit_Button]
        if A == 0:
            Buttons(screen, RED, 395, 195, 160, 85, 2, " ", "White", 395, 195)
        if A == 0 and Player_Input_SPACE == True:
            Main_Menu = False
            Player_Creation = True
            A = 0
            Player_Input_SPACE = False
        if A == 1:
            Buttons(screen, RED, 395, 295, 160, 85, 2, " ", "White", 395, 295)
        if A == 1 and Player_Input_SPACE == True:
            pygame.quit()

    if Player_Creation:
        Hea_Crea = Buttons(screen, BLACK, 90, 100, 100, 50, 50, "Health", "White", 95, 105)
        Att_Crea = Buttons(screen, BLACK, 90, 150, 100, 50, 50, "Attack", "White", 95, 155)
        Def_Crea = Buttons(screen, BLACK, 90, 200, 100, 50, 50, "Defense", "White", 95, 205)
        Init_Crea = Buttons(screen, BLACK, 90, 250, 100, 50, 50, "Initiative", "White", 95, 255)
        Spe_Crea = Buttons(screen, BLACK, 90, 300, 100, 50, 50, "Special", "White", 95, 305)
        List_of_Buttons_Y = [Hea_Crea, Att_Crea, Def_Crea, Init_Crea, Spe_Crea]
        List_of_Buttons_X = [Hea_Crea, Att_Crea]

        for x in range(5):
            Buttons(screen, "Green", 205, 105 + (x * 50), 20, 20, 0, "+", "White", 210, 105 + (x * 50))
            Buttons(screen, "Red", 255, 105 + (x * 50), 20, 20, 0, "-", "White", 260, 105 + (x * 50))

        for y in range(6):
            for l in range(2):
                if A == y and B == l:
                    Selection = Buttons(screen, RED, 200 + (50 * l), 100 + (50 * y), 30, 30, 2, "", "White", 0, 0)

            if Player_Input_SPACE == True and A == y and B == 0:
                Stats_Creation[A] += 1  # hier steigt es
                Stat_Points -= 1
                Player_Input_SPACE = False

            if Stats_Creation[A] == 0:  # für den fall eine Statistik wird kleiner 1
                Stats_Creation[A] = 1

            if Stat_Points > 20:
                Stat_Points = 20

            if Player_Input_SPACE == True and A == y and B == 1 and Stats_Creation[A] > 1:
                Stats_Creation[A] -= 1  # hier sinkt es
                Stat_Points += 1
                Player_Input_SPACE = False

            if Stats_Creation[A] > 10:  # für den fall eine Statistik wird größer 10
                Stat_Points += 1
                Stats_Creation[A] = 10

            if Stat_Points < 0:
                Stat_Points = 0

        for y in range(5):
            Buttons(screen, "Black", 305, 105 + (y * 50), 20, 20, 0, str(Stats_Creation[y]), "Blue", 312,
                    107 + (y * 50))
        Buttons(screen, "Black", 405, 105, 35, 20, 0, str(Stat_Points), "Blue", 412, 107)

        if Stat_Points == 0:
            Player = Character()
            Player.stats(Stats_Creation[0], Stats_Creation[1], Stats_Creation[2], Stats_Creation[4], Stats_Creation[3],
                         "Dominik")
            Player.Battle_Stats()
            A = 0
            B = 0
            Player_Creation = False
            Rest_Phase = True

    if Rest_Phase:
        # The coins
        pygame.draw.circle(screen, "Yellow", (20, 20), 10)
        Coins_Text = font.render("= " + str(Player.coins), False, "Black")
        screen.blit(Coins_Text, (40, 11))

        Start_Battle_Button = Buttons(screen, BLACK, 90, 100, 150, 80, 40, "Start The Fight", "White", 98, 125)
        Shop_Button = Buttons(screen, BLACK, 90, 300, 150, 80, 40, "Buy Items", "White", 120, 330)
        Check_Enemies_Button = Buttons(screen, BLACK, 700, 100, 150, 80, 40, "Enemies", "Grey", 740, 130)
        Forfeit_Button = Buttons(screen, BLACK, 700, 300, 150, 80, 40, "FORFEIT", "Grey", 740, 330)

        List_of_Buttons_X = [Start_Battle_Button, Check_Enemies_Button]
        List_of_Buttons_Y = [Start_Battle_Button, Shop_Button]
        match A:
            case 0:
                match B:
                    case 0:
                        pygame.draw.rect(screen, "Red", [90, 100, 150, 80], 2)
                        if Player_Input_SPACE:
                            Player_Input_SPACE, Rest_Phase = False, False
                            Battle, Stage1 = True, True
                            Enemy = Enemy_List[randint(0, 2)]
                            Enemy.Battle_Stats()
                    case 1:
                        pygame.draw.rect(screen, "Red", [700, 100, 150, 80], 2)
                        if Player_Input_SPACE:
                            Player_Input_SPACE, Rest_Phase = False, False
                            Enemy_view = True
            case 1:
                match B:
                    case 0:
                        pygame.draw.rect(screen, "Red", [90, 300, 150, 80], 2)
                        if Player_Input_SPACE:
                            Player_Input_SPACE = False
                            Rest_Phase = False
                            Shop = True
                    case 1:
                        pygame.draw.rect(screen, "Red", [700, 300, 150, 80], 2)

    if Shop:
        Buy_Health_Potion = Buttons(screen, BLACK, 90, 100, 170, 80, 0, "Buy Health Potion", "White", 98, 125)
        Buy_Special_Potion = Buttons(screen, BLACK, 730, 100, 170, 80, 0, "Buy Special Potion", "White", 738, 125)
        Buy_Item = Buttons(screen, BLACK, 110, 400, 650, 150, 0, Magic_Wand.name, "White", 155, 405)
        screen.blit(Magic_Wand_Description, (115, 430))

        List_of_Buttons_X = [Buy_Health_Potion, Buy_Special_Potion]
        List_of_Buttons_Y = [Buy_Item]

        # The Coins
        pygame.draw.circle(screen, "Yellow", (20, 20), 10)
        Coins_Text = font.render("= " + str(Player.coins), False, "Black")
        screen.blit(Coins_Text, (40, 11))

        if Player_Input_ALT:
            Shop = False
            Rest_Phase = True
            Player_Input_ALT = False

    if Enemy_view:
        if Player_Input_ALT:
            Enemy_view = False
            Rest_Phase = True
            Player_Input_ALT = False

    if Battle:
        Round_Counter_Text = font.render(str(Round_Counter), False, "Black")
        screen.blit(Round_Counter_description, (800, 70))
        screen.blit(Round_Counter_Text, (850, 100))
        # Das sind die Healthbars von Player
        Player_Healthbar = Bar(screen, "Green", 400, 500, 200, 20, 2, Player.Battle_Health_Actual,
                               Player.Battle_Health_Max, BLACK, 555, 501)
        Player_Specialbar = Bar(screen, "Blue", 400, 520, 200, 20, 2, Player.Battle_Special_Actual,
                                Player.Battle_Special_Max, BLACK, 555, 521)

        # Das sind die Healthbars von Enemy
        Enemy_Healthbar = Bar(screen, "Red", 400, 20, 200, 20, 2, Enemy.Battle_Health_Actual,
                              Enemy.Battle_Health_Max, BLACK, 555, 21)
        Enemy_Healthbar = Bar(screen, "Violet", 400, 40, 200, 20, 2, Enemy.Battle_Special_Actual,
                              Enemy.Battle_Special_Max, BLACK, 555, 41)

        screen.blit(Player_picture, (500, 350))
        screen.blit(Enemy_picture, (500, 150))
        if TurnOrder == 1:
            if Stage1:  # Battle Menu
                Attack_Button = Buttons(screen, BLACK, 10, 20, 200, 100, 100, "Attack", "White", 10, 20)
                Defend_Button = Buttons(screen, BLACK, 10, 130, 200, 100, 100, "Defense", "White", 10, 130)
                Special_Button = Buttons(screen, BLACK, 10, 240, 200, 100, 100, "Special", "White", 10, 240)
                Items_Button = Buttons(screen, BLACK, 10, 350, 200, 100, 100, "Items", "White", 10, 350)
                List_of_Buttons_X = [Attack_Button]
                List_of_Buttons_Y = [Attack_Button, Defend_Button, Special_Button, Items_Button]

                if Round_Counter == temp_round_att + 3:
                    Player.Battle_Attack_Actual = Player.Battle_Attack_Max
                if Round_Counter == temp_round_def + 3:
                    Player.Battle_Defense_Actual = Player.Battle_Defense_Max

                if not Player_Input_SPACE:
                    match A:
                        case 0:
                            Buttons(screen, RED, 5, 15, 210, 110, 2, " ", "White", 0, 0)

                        case 1:
                            Buttons(screen, RED, 5, 125, 210, 110, 2, " ", "White", 0, 0)

                        case 2:
                            Buttons(screen, RED, 5, 235, 210, 110, 2, " ", "White", 0, 0)

                        case 3:
                            Buttons(screen, RED, 5, 345, 210, 110, 2, " ", "White", 0, 0)
                if Player_Input_SPACE:
                    Stage2 = True
                    Stage1 = False
                    Player_Input_SPACE = False

            ########################################### Untermenüs ###################################################

            if Stage2:
                match A:
                    case 0:
                        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
                        screen.blit(Sword_text, (20, 20))
                        screen.blit(Bow_text, (20, 40))
                        match B:
                            case 0:
                                pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)
                                if Player_Input_SPACE:
                                    damage(Player, Enemy)
                                    SwitchTurns()
                            case 0:
                                pygame.draw.rect(screen, RED, [10, 40, 200, 20], 2)
                                if Player_Input_SPACE:
                                    damage(Player, Enemy)
                                    SwitchTurns()
                    case 1:
                        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
                        screen.blit(Shield_text, (20, 20))
                        pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)
                        match B:
                            case 0:
                                pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)
                                if Player_Input_SPACE:
                                    Player.Defend()
                                    SwitchTurns()
                    case 2:
                        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
                        screen.blit(Attck_Buff_text, (20, 20))
                        screen.blit(Defense_Buff_text, (20, 40))
                        match B:
                            case 0:
                                pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)
                                if Player_Input_SPACE:
                                    Player.setSpecial(-1)
                                    if Player.Battle_Special_Actual < 0:
                                        print("You don't have enough mana!")
                                        Player.setSpecial(1)
                                    else:
                                        Player.setAttack(1.2)
                                        temp_round_att = Round_Counter
                                        Buttons(screen, "Green", 400, 490, 20, 20, 3, "AttBuff", "Black", 400, 490)
                                        SwitchTurns()
                            case 1:
                                pygame.draw.rect(screen, RED, [10, 40, 200, 20], 2)
                                if Player_Input_SPACE:
                                    Player.setSpecial(-1)
                                    if Player.Battle_Special_Actual < 0:
                                        print("You don't have enough mana!")
                                        Player.setSpecial(1)
                                    else:
                                        Player.setDefense(1.2)
                                        temp_round_def = Round_Counter
                                        Buttons(screen, "Blue", 400, 490, 20, 20, 3, "DefBuff", "Black", 400, 490)
                                        SwitchTurns()
                    case 3:
                        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
                        screen.blit(Item_text, (20, 20))
                        pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)
            if Player_Input_ALT:
                Stage1 = True
                Stage2 = False
                Player_Input_ALT = False

        if TurnOrder == 2:

            Enemy_move = randint(1, 100)
            if Enemy_move < 70:
                damage(Enemy, Player)
                SwitchTurns()
                Round_Counter += 1
            if 70 <= Enemy_move < 90:
                Enemy.Defend()
                SwitchTurns()
                Round_Counter += 1
            if 90 <= Enemy_move < 95:
                print("Enemy used Item")
                Round_Counter += 1
                SwitchTurns()
            if Enemy_move >= 95:
                print("Enemy is sad and won't attack")
                Round_Counter += 1
                SwitchTurns()

            print(Enemy_move, Round_Counter)
        if Player.Battle_Health_Actual <= 0:
            Buttons(screen, "Black", 100, 80, 400, 400, 200, "YOU DIED", "Red", 200, 200)
            Battle = False
            Main_Menu = True
        if Enemy.Battle_Health_Actual <= 0:
            Buttons(screen, "Black", 100, 80, 400, 400, 200, "YOU WON", "Yellow", 200, 200)
            Battle = False
            Rest_Phase = True

        # print(A, B, Stage1, Stage2)
        print(Player.Battle_Attack_Actual, Player.Battle_Defense_Actual)
        print(Enemy.name)
        print(Player.Battle_Special_Actual, Player.Battle_Special_Max)
    Frames.tick(60)
    # print (Player_Input_ALT)

    print(Shop, len(List_of_Buttons_Y), len(List_of_Buttons_X), B, A)
