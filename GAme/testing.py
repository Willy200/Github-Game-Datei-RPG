import pygame
from Character import Character
#from Commands import darstellreihenfolge
from sys import exit
pygame.init()

class Buttons:
    Up = False
    Down = False
    def __init__(self, screen, color, XPos, YPos, XLen, YLen, Willyszahl, Text, TextColor): #Man kann die vorbestimmte Farben wie RED = (255, 0, 0) sowohl bei rect als auch bei Text benutzen
        pygame.draw.rect(screen, color, [XPos, YPos, XLen, YLen], Willyszahl)
        Buttons_Text = font.render(Text, False, TextColor)
        screen.blit(Buttons_Text, (XPos, YPos))
def UP_DOWN():
    global A
    global Stage1
    if event.type == pygame.KEYDOWN and Stage1 == True:
        if event.key == pygame.K_UP and Key_pressed == True:
            A -= 1
            if A == 0:
                A = 4
        elif event.key == pygame.K_DOWN and Key_pressed == True:
            A += 1
            if A == 5:
                A = 1
    elif event.type == pygame.KEYDOWN and Stage1 == False:
        if event.key == pygame.K_UP and Key_pressed == True:
            A = 1
        elif event.key == pygame.K_DOWN and Key_pressed == True:
            A = 0

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Spiel")
Frames = pygame.time.Clock()
font = pygame.font.Font("Fonts/Pixeltype.ttf", 30)

################################### Variablen definiert, damit Global ########################################################################
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

A = 1  # Gibt die Stufe in Stage1 an die gerade ausgewählt und Angezeigt wird
B = 1  # Gibt die Stufe in Stage2 Attack_Untermenü an die gerade ausgewählt und Angezeigt wird

Attack_Untermenü = False
Defende_Untermenü = False
Special_Untermenü = False
Item_Untermenü = False
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
surface2.fill("Blue")
# surface.fill("Red")############################################################################
Background.fill("White")
sky = pygame.image.load("Graphics/Sky.png")
ground = pygame.image.load("Graphics/ground.png")
########text = font.render("Player1",False,"Black")
text2 = font.render("Enemy", False, "Black")
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
    screen.blit(text2, (700, 180))
    # screen.blit(surface3,(0,300))
    # screen.blit(Background,(0,0))
    # Zustand  A (Attack gedrückt)

    ################### ERSTE MENÜ UND INPUT PHASE ##################################################################

    #screen.blit(Commands.darstellreihenfolge(), (20, 40))
    #if Textanzeige == True:
   # screen.blit(Text[i], (20, 40))

    #if i == 3:
       # Textanzeige = False
       # Stage1 = True

    # for x in range(2):
    # i = darstellreihenfolge(Text)
    # screen.blit(Text[i], (20, 40)

    if Stage1 == True: # Battle Menu
        Attack_Button = Buttons(screen, BLACK, 10, 20, 200, 100, 100, "Attack", "White")
        Defend_Button = Buttons(screen, BLACK, 10, 130, 200, 100, 100, "Defense", "White")
        Special_Button = Buttons(screen, BLACK, 10, 240, 200, 100, 100, "Special", "White")
        Items_Button = Buttons(screen, BLACK, 10, 350, 200, 100, 100, "Items", "White")

        if A > 4:
            A = 1
        if A < 1:
            A = 4
        if A == 1:

            Buttons(screen, RED, 5, 15, 210, 110, 2, " ", "White")
            Attack_Untermenü = True
        else:
            Attack_Untermenü = False
        if A == 2:
            Buttons(screen, RED, 5, 125, 210, 110, 2, " ", "White")
            Defende_Untermenü = True
        else:
            Defende_Untermenü = False
        if A == 3:
            Buttons(screen, RED, 5, 235, 210, 110, 2, " ", "White")
            Special_Untermenü = True
        else:
            Special_Untermenü = False
        if A == 4:
            Buttons(screen, RED, 5, 345, 210, 110, 2, " ", "White")
            Item_Untermenü = True
        else:
            Item_Untermenü = False





        Player_Input_ALT = False  # Wichig! Damit A und B zurückgesetzt werden, wenn man die Stage wechselt.
    elif Main_Menu == True:
        Start_Button = Buttons(screen, BLACK, 400, 200, 150, 75, 100, "Start", "White")
        Exit_Button = Buttons(screen, BLACK, 400, 300, 150, 75, 100, "Quit", "White")
        if A == 1:
            Buttons(screen, RED, 395, 195, 160, 85, 2, " ", "White")
        elif A == 1 and Player_Input_SPACE == True:
            Main_Menu = False
            Stage1 = 1
        else:
            Buttons(screen, RED, 395, 295, 160, 85, 2, " ", "White")


    if Player_Input_SPACE == True :
        # if A == 1 or A == 2:
        Stage1 = False
        Stage2 = True
        # else:                                        # vieleicht später noch wichtig
        # Player_Input_SPACE = False
    if Player_Input_ALT == True:
        Stage1 = True
        Stage2 = False
        A = 1  # Wichig! Damit A und B zurückgesetzt werden, wenn man die Stage wechselt.
        B = 1  # Wichig! Damit A und B zurückgesetzt werden, wenn man die Stage wechselt.
    ########################################### Untermenüs ###############################################################

    if Stage2 == True and Attack_Untermenü == True:
        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
        screen.blit(Sword_text, (20, 20))
        screen.blit(Bow_text, (20, 40))

        if B >= 2:  # Damit B auch nur zwischen 1 und 2 bleibt
            B = 2
        if B <= 1:
            B = 1

        if B == 1:  # zeichnen von roten Kasten um Bow und Sword in Attack_Untermenü
            pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)

        if B == 2:
            pygame.draw.rect(screen, RED, [10, 40, 200, 20], 2)

    if Stage2 == True and Defende_Untermenü == True:
        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
        screen.blit(Shield_text, (20, 20))
        pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)

    if Stage2 == True and Special_Untermenü == True:

        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
        screen.blit(Attck_Buff_text, (20, 20))
        screen.blit(Defense_Buff_text, (20, 40))
        if B >= 2:  # Damit B auch nur zwischen 1 und 2 bleibt
            B = 2
        if B <= 1:
            B = 1

        if B == 1:  # zeichnen von roten Kasten um Bow und Sword in Attack_Untermenü
            pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)

        if B == 2:
            pygame.draw.rect(screen, RED, [10, 40, 200, 20], 2)

    if Stage2 == True and Item_Untermenü == True:
        pygame.draw.rect(screen, BLACK, [10, 20, 200, 300], 100)
        screen.blit(Item_text, (20, 20))
        pygame.draw.rect(screen, RED, [10, 20, 200, 20], 2)
    print(A)
    print(Player_Input_SPACE)
    Frames.tick(60)
