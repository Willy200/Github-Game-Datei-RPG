import pygame
from Character import Character
from sys import exit
from Commands import damage
from random import *

pygame.init()


class Buttons:
    def __init__(self, screen, color, XPos, YPos, XLen, YLen, Willyszahl, Text, TextColor, XPos_Text,
                 YPos_Text):  # Man kann die vorbestimmte Farben wie RED = (255, 0, 0) sowohl bei rect als auch bei Text benutzen
        pygame.draw.rect(screen, color, [XPos, YPos, XLen, YLen], Willyszahl)
        Buttons_Text = font.render(Text, False, TextColor)
        screen.blit(Buttons_Text, (XPos_Text, YPos_Text))


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


def SwitchTurns():
    global A
    global Stage1
    global Stage2
    global TurnOrder
    global Player_Input_SPACE
    A = 1
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

################################### Variablen definiert, damit Global ########################################################################
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Round_Counter = 0
Player_Buff = False
Battle = False
A = 1  # Gibt die Stufe in Stage1 an die gerade ausgewählt und Angezeigt wird
B = 1  # Gibt die Stufe in Stage2 Attack_Untermenü an die gerade ausgewählt und Angezeigt wird
Shop = False
TurnOrder = 1
Stat_Points = 2
Stats_Creation = [1, 1, 1, 1, 1]
temp_round_att = 0
temp_round_def = 0
Rest_Phase = False
Player_Creation = False
Attack_Untermenü = False
Defende_Untermenü = False
Special_Untermenü = False
Item_Untermenü = False
Player_Input_DOWN = False
Player_Input_UP = False
Player_Input_SPACE = False
Player_Input_ALT = False
Player_Input_RIGHT = False
Player_Input_LEFT = False
Stage1 = False
Stage2 = False
Main_Menu = True
Textanzeige = True
Background = pygame.Surface((1000, 600))
surface3 = pygame.Surface((200, 50))
surface3.fill("Red")
Background.fill("White")
sky = pygame.image.load("Graphics/Sky.png")
ground = pygame.image.load("Graphics/ground.png")
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
################################################################### Text darstellen ##################################################
i = 0
T1 = font.render("Welcome to the new Turnamento", False, "Black")
T2 = font.render("These formidble Worriors will be your Opponent", False, "Black")
T3 = font.render("Can you beat them all ? Will you be the new Champion? ", False, "Black")
T4 = font.render(" ", False, "Black")
Text = [T1, T2, T3, T4]
# screen.blit(Text[i], (20, 40))
##################################################################### main Game loop ###################################################################################
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # guckt ob exit gedückt wird(wichtig um Fenster zu schließen)

            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:  # Das alles hier guck ob eine Taste gedrückt wurde. Wenn sie gedrückt wird ist die entsprechende Input Variable auf TRUE gesetzt, sonst nicht. Alle anderen sind False.
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
        UP_DOWN()
    pygame.display.update()
    screen.blit(Background, (0, 0))

    ################### ERSTE MENÜ UND INPUT PHASE ##################################################################

    if Main_Menu:
        Start_Button = Buttons(screen, BLACK, 400, 200, 150, 75, 100, "Start", "White", 450, 220)
        Exit_Button = Buttons(screen, BLACK, 400, 300, 150, 75, 100, "Quit", "White", 450, 320)
        if A == 1:
            Buttons(screen, RED, 395, 195, 160, 85, 2, " ", "White", 395, 195)
        if A == 1 and Player_Input_SPACE == True:
            Main_Menu = False
            Player_Creation = True
            A = 1
            Player_Input_SPACE = False
        if A == 0:
            Buttons(screen, RED, 395, 295, 160, 85, 2, " ", "White", 395, 295)
        if A == 0 and Player_Input_SPACE == True:
            pygame.quit()

    if Player_Creation:
        Hea_Crea = Buttons(screen, BLACK, 90, 100, 100, 50, 50, "Health", "White", 95, 105)
        Att_Crea = Buttons(screen, BLACK, 90, 150, 100, 50, 50, "Attack", "White", 95, 155)
        Def_Crea = Buttons(screen, BLACK, 90, 200, 100, 50, 50, "Defense", "White", 95, 205)
        Init_Crea = Buttons(screen, BLACK, 90, 250, 100, 50, 50, "Initiative", "White", 95, 255)
        Spe_Crea = Buttons(screen, BLACK, 90, 300, 100, 50, 50, "Special", "White", 95, 305)

        for x in range(5):
            Buttons(screen, "Green", 205, 105 + (x * 50), 20, 20, 0, "+", "White", 210, 105 + (x * 50))
            Buttons(screen, "Red", 255, 105 + (x * 50), 20, 20, 0, "-", "White", 260, 105 + (x * 50))

        for y in range(6):
            for l in range(2):
                if A == y + 1 and B == l + 1:
                    Selection = Buttons(screen, RED, 200 + (50 * l), 100 + (50 * y), 30, 30, 2, "", "White", 0, 0)

            if Player_Input_SPACE == True and A == y + 1 and B == 1:
                Stats_Creation[A - 1] += 1  # hier steigt es
                Stat_Points -= 1
                Player_Input_SPACE = False

            if Stats_Creation[A - 1] == 0:  # für den fall eine Statistik wird kleiner 1
                Stats_Creation[A - 1] = 1

            if Stat_Points > 20:
                Stat_Points = 20

            if Player_Input_SPACE == True and A == y + 1 and B == 2 and Stats_Creation[A - 1] > 1:
                Stats_Creation[A - 1] -= 1  # hier sinkt es
                Stat_Points += 1
                Player_Input_SPACE = False

            if Stats_Creation[A - 1] > 10:  # für den fall eine Statistik wird größer 10
                Stat_Points += 1
                Stats_Creation[A - 1] = 10

            if Stat_Points < 0:
                Stat_Points = 0

        for y in range(5):
            Buttons(screen, "Black", 305, 105 + (y * 50), 20, 20, 0, str(Stats_Creation[y]), "Blue", 312,
                    107 + (y * 50))
        Buttons(screen, "Black", 405, 105, 35, 20, 0, str(Stat_Points), "Blue", 412, 107)

        if Stat_Points == 0:
            Player = Character()
            Player.stats(Stats_Creation[0], Stats_Creation[1], Stats_Creation[2], Stats_Creation[3], Stats_Creation[4],
                         "Dominik")
            Player.Battle_Stats()
            A = 1
            B = 1
            Enemy = Character()
            Enemy.stats(Stats_Creation[0], Stats_Creation[1], Stats_Creation[2], Stats_Creation[3], Stats_Creation[4],
                        "Willy")
            Enemy.Battle_Stats()
            #Battle = True
            Player_Creation = False
            Rest_Phase = True

    if Rest_Phase:
        Start_Battle_Button = Buttons(screen, BLACK, 90, 100, 150, 80, 40, "Start The Fight", "White", 98, 125)
        Shop_Button = Buttons(screen, BLACK, 90, 300, 150, 80, 40, "Buy Items", "White", 120, 330)
        Check_Enemies_Button = Buttons(screen, BLACK, 700, 100, 150, 80, 40, "Enemies", "Grey", 740, 130)
        Forfeit_Button = Buttons(screen, BLACK, 700, 300, 150, 80, 40, "FORFEIT", "Grey", 740, 330)
        match A:
            case 1:
                match B:
                    case 1:
                        pygame.draw.rect(screen, "Red", [90, 100, 150, 80], 2)
                        if Player_Input_SPACE:
                            Player_Input_SPACE, Rest_Phase = False, False
                            Battle, Stage1 = True, True
                    case 2:
                        pygame.draw.rect(screen, "Red", [700, 100, 150, 80], 2)

            case 2:
                match B:
                    case 1:
                        pygame.draw.rect(screen, "Red", [90, 300, 150, 80], 2)
                        if Player_Input_SPACE:
                            Player_Input_SPACE = False
                            Rest_Phase = False
                            Shop = True
                    case 2:
                        pygame.draw.rect(screen, "Red", [700, 300, 150, 80], 2)

    if Shop:
        Buy_Health_Potion = Buttons(screen, BLACK, 90, 100, 150, 80, 40, "Buy Health Potion", "White", 98, 125)
        Buy_Special_Potion = Buttons(screen, BLACK, 90, 300, 150, 80, 40, "Buy Special Potion", "White", 120, 330)
        Buy_Item = Buttons(screen, BLACK, 700, 100, 150, 300, 75, "Buy Item", "White", 737, 250)

    if Battle:
        # Das sind die Healthbars von Player
        pygame.draw.rect(screen, "Green", [400, 500, 200, 20], 2)
        Player_Healthbar = Buttons(screen, "Green", 400, 500,
                                   200 * (Player.Battle_Health_Actual / Player.Battle_Health_Max), 20, 20,
                                   str((Player.Battle_Health_Actual / Player.Battle_Health_Max) * 100)[0:3] + "%",
                                   BLACK, 555, 501)
        pygame.draw.rect(screen, "Blue", [400, 520, 200, 20], 2)
        pygame.draw.rect(screen, "Blue",
                         [400, 520, 200 * (Player.Battle_Special_Actual / Player.Battle_Special_Max), 20], 20)

        Player_Specialbar = Buttons(screen, "Blue", 400, 520,
                                    200 * (Player.Battle_Special_Actual / Player.Battle_Special_Max), 20, 20,
                                    str((Player.Battle_Special_Actual / Player.Battle_Special_Max) * 100)[0:3] + "%",
                                    BLACK, 555, 521)

        # Das sind die Healthbars von Enemy
        pygame.draw.rect(screen, "Red", [400, 20, 200, 20], 2)
        pygame.draw.rect(screen, "Red", [400, 20, 200 * (Enemy.Battle_Health_Actual / Enemy.Battle_Health_Max), 20], 20)
        Enemy_Healthbar = Buttons(screen, "Red", 400, 20,
                                  200 * (Enemy.Battle_Health_Actual / Enemy.Battle_Health_Max), 20, 20,
                                  str((Enemy.Battle_Health_Actual / Enemy.Battle_Health_Max) * 100)[0:3] + "%",
                                  BLACK, 555, 21)

        pygame.draw.rect(screen, "Blue", [400, 520, 200, 20], 2)
        pygame.draw.rect(screen, "Violet", [400, 40, 200, 20], 2)
        Enemy_Specialbar = Buttons(screen, "Violet", 400, 40,
                                   200 * (Enemy.Battle_Special_Actual / Enemy.Battle_Special_Max), 20, 20,
                                   str((Enemy.Battle_Special_Actual / Enemy.Battle_Special_Max) * 100)[0:3] + "%",
                                   BLACK, 555, 41)

        if TurnOrder == 1:
            if Stage1:  # Battle Menu
                Attack_Button = Buttons(screen, BLACK, 10, 20, 200, 100, 100, "Attack", "White", 10, 20)
                Defend_Button = Buttons(screen, BLACK, 10, 130, 200, 100, 100, "Defense", "White", 10, 130)
                Special_Button = Buttons(screen, BLACK, 10, 240, 200, 100, 100, "Special", "White", 10, 240)
                Items_Button = Buttons(screen, BLACK, 10, 350, 200, 100, 100, "Items", "White", 10, 350)

                if Round_Counter == temp_round_att + 3:
                    Player.Battle_Attack_Actual = Player.Battle_Attack_Max
                if Round_Counter == temp_round_def + 3:
                    Player.Battle_Defense_Actual = Player.Battle_Defense_Max

                if not Player_Input_SPACE:
                    match A:
                        case 1:
                            Buttons(screen, RED, 5, 15, 210, 110, 2, " ", "White", 0, 0)

                        case 2:
                            Buttons(screen, RED, 5, 125, 210, 110, 2, " ", "White", 0, 0)

                        case 3:
                            Buttons(screen, RED, 5, 235, 210, 110, 2, " ", "White", 0, 0)

                        case 4:
                            Buttons(screen, RED, 5, 345, 210, 110, 2, " ", "White", 0, 0)
                if Player_Input_SPACE:
                    Stage2 = True
                    Stage1 = False
                    Player_Input_SPACE = False

            ########################################### Untermenüs ###############################################################

            if Stage2:
                match A:
                    case 1:
                        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
                        screen.blit(Sword_text, (20, 20))
                        screen.blit(Bow_text, (20, 40))
                        match B:
                            case 1:
                                pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)
                                if Player_Input_SPACE:
                                    damage(Player, Enemy)
                                    SwitchTurns()
                            case 2:
                                pygame.draw.rect(screen, RED, [10, 40, 200, 20], 2)
                    case 2:
                        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
                        screen.blit(Shield_text, (20, 20))
                        pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)
                        match B:
                            case 1:
                                pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)
                                if Player_Input_SPACE:
                                    Player.Defend()
                                    SwitchTurns()
                    case 3:
                        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
                        screen.blit(Attck_Buff_text, (20, 20))
                        screen.blit(Defense_Buff_text, (20, 40))
                        match B:
                            case 1:
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
                            case 2:
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
                    case 4:
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
            if Enemy_move >= 70 and Enemy_move < 90:
                Enemy.Defend()
                SwitchTurns()
                Round_Counter += 1
            if Enemy_move >= 90 and Enemy_move < 95:
                print("Enemy used Item")
                Round_Counter += 1
            if Enemy_move >= 95 and Enemy_move <= 100:
                print("Enemy is sad and won't attack")
                Round_Counter += 1

            print(Enemy_move, Round_Counter)
        if Player.Battle_Health_Actual <= 0:
            Buttons(screen, "Black", 100, 80, 400, 400, 200, "YOU DIED", "Red", 200, 200)
        if Enemy.Battle_Health_Actual <= 0:
            Buttons(screen, "Black", 100, 80, 400, 400, 200, "YOU WON", "Yellow", 200, 200)

    #print(A, B, Stage1, Stage2)
        print(Player.Battle_Attack_Actual, Player.Battle_Defense_Actual)
    Frames.tick(60)
