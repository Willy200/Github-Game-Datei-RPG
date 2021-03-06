import pygame
from Character import Character
# from Commands import darstellreihenfolge
from sys import exit

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

    if event.type == pygame.KEYDOWN and Stage1 == True:
        if event.key == pygame.K_UP and Key_pressed == True:
            A -= 1
            if A == 0:
                A = 4

        elif event.key == pygame.K_DOWN and Key_pressed == True:
            A += 1
            if A == 5:
                A = 1

    elif event.type == pygame.KEYDOWN and Main_Menu == True:
        if event.key == pygame.K_UP and Key_pressed == True:
            A = 1

        elif event.key == pygame.K_DOWN and Key_pressed == True:
            A = 0

    elif event.type == pygame.KEYDOWN and Player_Creation == True:
        if event.key == pygame.K_DOWN and Key_pressed == True:
            A += 1
            if A == 6:
                A = 1

        if event.key == pygame.K_UP and Key_pressed == True:
            A -= 1
            if A == 0:
                A = 1
        if event.key == pygame.K_LEFT and Key_pressed == True:
            B -= 1
            if B == 0:
                B = 1
        if event.key == pygame.K_RIGHT and Key_pressed == True:
            B += 1
            if B == 3:
                B = 2


screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Spiel")
Frames = pygame.time.Clock()
font = pygame.font.Font("Fonts/Pixeltype.ttf", 30)

################################### Variablen definiert, damit Global ########################################################################
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

A = 1  # Gibt die Stufe in Stage1 an die gerade ausgew??hlt und Angezeigt wird
B = 1  # Gibt die Stufe in Stage2 Attack_Untermen?? an die gerade ausgew??hlt und Angezeigt wird
Stat_Points = 20
Stats_Creation = [1, 1, 1, 1, 1]
Player_Creation = False
Attack_Untermen?? = False
Defende_Untermen?? = False
Special_Untermen?? = False
Item_Untermen?? = False
Player_Input_DOWN = False
Player_Input_UP = False
Key_pressed = False
Player_Input_SPACE = False
Player_Input_ALT = False
Stage1 = False
Stage2 = False
Main_Menu = True
Textanzeige = True
Background = pygame.Surface((1000, 600))
# surface = pygame.Surface((100,200))##########################################################
surface2 = pygame.Surface((100, 200))
surface3 = pygame.Surface((200, 50))
surface3.fill("Red")
# surface2.fill("Blue")
# surface.fill("Red")############################################################################
Background.fill("White")
sky = pygame.image.load("Graphics/Sky.png")
ground = pygame.image.load("Graphics/ground.png")
########text = font.render("Player1",False,"Black")
# text2 = font.render("Enemy", False, "Black")
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
        if event.type == pygame.QUIT:  # guckt ob exit ged??ckt wird(wichtig um Fenster zu schlie??en)

            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:  # Das alles hier guck ob eine Taste gedr??ckt wurde. Wenn sie gedr??ckt wird ist die entsprechende Input Variable auf TRUE gesetzt, sonst nicht. Alle anderen sind False.
            Key_pressed = True
            UP_DOWN()

            if event.key == pygame.K_RIGHT and Key_pressed == True:
                Payer_Input_RIGHT = True
            else:
                Payer_Input_RIGHT = False

            if event.key == pygame.K_LEFT and Key_pressed == True:
                Player_Input_LEFT = True
            else:
                Payer_Input_LEFT = False
            if event.key == pygame.K_SPACE and Key_pressed == True:
                Player_Input_SPACE = True
                Player_Input_ALT = False
            else:
                Payer_Input_SPACE = False

            if event.key == pygame.K_m and Key_pressed == True:
                Player_Input_ALT = True
                Player_Input_SPACE = False
            else:
                Payer_Input_SPACE = False
    Key_pressed = False
    pygame.display.update()
    screen.blit(Background, (0, 0))
    # screen.blit(sky,(0,0))
    # screen.blit(ground,(0,350))
    # screen.blit(surface,(400,200))#############################################
    screen.blit(surface2, (700, 200))
    ####screen.blit(text,(400,180))
    # screen.blit(text2, (700, 180))
    # screen.blit(surface3,(0,300))
    # screen.blit(Background,(0,0))
    # Zustand  A (Attack gedr??ckt)

    ################### ERSTE MEN?? UND INPUT PHASE ##################################################################

    # screen.blit(Commands.darstellreihenfolge(), (20, 40))
    # if Textanzeige == True:
    # screen.blit(Text[i], (20, 40))

    # if i == 3:
    # Textanzeige = False
    # Stage1 = True

    # for x in range(2):
    # i = darstellreihenfolge(Text)
    # screen.blit(Text[i], (20, 40)

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

            if Stats_Creation[A - 1] == 0:  # f??r den fall eine Statistik wird kleiner 1
                # Stat_Points += 1
                Stats_Creation[A - 1] = 1

            if Stat_Points > 20:
                Stat_Points = 20

            if Player_Input_SPACE == True and A == y + 1 and B == 2 and Stats_Creation[A - 1] > 1:
                Stats_Creation[A - 1] -= 1  # hier sinkt es
                Stat_Points += 1
                Player_Input_SPACE = False

            if Stats_Creation[A - 1] > 10:  # f??r den fall eine Statistik wird gr????er 10
                Stat_Points += 1
                Stats_Creation[A - 1] = 10

            if Stat_Points < 0:
                Stat_Points = 0

        for y in range(5):
            Buttons(screen, "Black", 305, 105 + (y * 50), 20, 20, 0, str(Stats_Creation[y]), "Blue", 312, 107 + (y * 50))
        Buttons(screen, "Black", 405, 105, 35, 20, 0, str(Stat_Points), "Blue", 412, 107)

        if Stat_Points == 0:
            Stage1 = True
            Player_Creation = False
            Player = Character()
            Player.stats(Stats_Creation[0], Stats_Creation[1], Stats_Creation[2], Stats_Creation[3], Stats_Creation[4], "Dominik")
            A = 1

    if Stage1:  # Battle Menu
        Attack_Button = Buttons(screen, BLACK, 10, 20, 200, 100, 100, "Attack", "White", 10, 20)
        Defend_Button = Buttons(screen, BLACK, 10, 130, 200, 100, 100, "Defense", "White", 10, 130)
        Special_Button = Buttons(screen, BLACK, 10, 240, 200, 100, 100, "Special", "White", 10, 240)
        Items_Button = Buttons(screen, BLACK, 10, 350, 200, 100, 100, "Items", "White", 10, 350)

        if A > 4:
            A = 1
        if A < 1:
            A = 4
        if A == 1:
            Buttons(screen, RED, 5, 15, 210, 110, 2, " ", "White", 0,0)
            Attack_Untermen?? = True
        else:
            Attack_Untermen?? = False
        if A == 2:
            Buttons(screen, RED, 5, 125, 210, 110, 2, " ", "White", 0,0)
            Defende_Untermen?? = True
        else:
            Defende_Untermen?? = False
        if A == 3:
            Buttons(screen, RED, 5, 235, 210, 110, 2, " ", "White", 0,0)
            Special_Untermen?? = True
        else:
            Special_Untermen?? = False
        if A == 4:
            Buttons(screen, RED, 5, 345, 210, 110, 2, " ", "White", 0,0)
            Item_Untermen?? = True
        else:
            Item_Untermen?? = False

        Player_Input_ALT = False  # Wichig! Damit A und B zur??ckgesetzt werden, wenn man die Stage wechselt.

    # if Player_Input_SPACE == True :
    # if A == 1 or A == 2:
    #    Stage1 = False
    #   Stage2 = True
    # else:                                        # vieleicht sp??ter noch wichtig
    # Player_Input_SPACE = False
    # if Player_Input_ALT == True:
    #    Stage1 = True
    #   Stage2 = False
       # A = 1  # Wichig! Damit A und B zur??ckgesetzt werden, wenn man die Stage wechselt.
    # B = 1  # Wichig! Damit A und B zur??ckgesetzt werden, wenn man die Stage wechselt.
    ########################################### Untermen??s ###############################################################

    if Stage2 == True and Attack_Untermen?? == True:
        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
        screen.blit(Sword_text, (20, 20))
        screen.blit(Bow_text, (20, 40))

        if B >= 2:  # Damit B auch nur zwischen 1 und 2 bleibt
            B = 2
        if B <= 1:
            B= 1

        if B == 1:  # zeichnen von roten Kasten um Bow und Sword in Attack_Untermen??
            pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)

        if B == 2:
            pygame.draw.rect(screen, RED, [10, 40, 200, 20], 2)


    #if Player_Input_SPACE == True :
    # if A == 1 or A == 2:

        #Stage1 = False
        #Stage2 = True
    if Player_Input_ALT == True:
        Stage1 = True
        Stage2 = False

    if Stage2 == True and Defende_Untermen?? == True:
        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
        screen.blit(Shield_text, (20, 20))
        pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)

    if Stage2 == True and Special_Untermen?? == True:

        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
        screen.blit(Attck_Buff_text, (20, 20))
        screen.blit(Defense_Buff_text, (20, 40))
        if B >= 2:  # Damit B auch nur zwischen 1 und 2 bleibt
            B= 2
        if B <= 1:
            B = 1

        if B == 1:  # zeichnen von roten Kasten um Bow und Sword in Attack_Untermen??
            pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)

        if B == 2:
            pygame.draw.rect(screen, RED, [10, 40, 200, 20], 2)

    if Stage2 == True and Item_Untermen?? == True:
        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
        screen.blit(Item_text, (20, 20))
        pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)

    #print(Stats_Creation, Stat_Points)
    print(Player_Input_SPACE)
    print(A)
    Frames.tick(60)
