import pygame
from Character import Character
#from Commands import darstellreihenfolge
from sys import exit

pygame.init()

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
Stage1 = True
Stage2 = False
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
Attack_text = font.render("ATTACK", False, "White")
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



        elif event.type == pygame.KEYDOWN:  # Das alles hier guck ob eine Taste gedrückt wurde. Wenn sie gedrückt wird ist die entsprechende Input Variable auf TRUE gesetzt, sonst nicht. Alle anderen sind Fals.
            Key_pressed = True

            if event.key == pygame.K_RIGHT and Key_pressed == True:
                Payer_Input_RIGHT = True
            else:
                Payer_Input_RIGHT = False

            if event.key == pygame.K_LEFT and Key_pressed == True:
                Player_Input_LEFT = True
            else:
                Payer_Input_LEFT = False

            if event.key == pygame.K_UP and Key_pressed == True:
                Player_Input_UP = True
                if Stage1 == True:
                    A = A - 1
                if Stage1 == True:
                    B = B - 1
            else:
                Player_Input_UP = False

            if event.key == pygame.K_DOWN and Key_pressed == True:
                Player_Input_DOWN = True
                if Stage1 == True:
                    A = A + 1
                if Stage2 == True:
                    B = B + 1
            else:
                Payer_Input_DOWN = False

            if event.key == pygame.K_SPACE and Key_pressed == True:
                #darstellreihenfolge(Text)

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
    # screen.blit(Text[i], (20, 40))

    if Stage1 == True :

        if A > 4:
            A = 1
        if A < 1:
            A = 4

        if A == 1:
            pygame.draw.rect(screen, RED, [5, 15, 210, 110], 2)
            Attack_Untermenü = True
        else:
            Attack_Untermenü = False

        if A == 2:
            pygame.draw.rect(screen, RED, [5, 125, 210, 110], 2)
            Defende_Untermenü = True
        else:
            Defende_Untermenü = False

        if A == 3:
            pygame.draw.rect(screen, RED, [5, 235, 210, 110], 2)
            Special_Untermenü = True
        else:
            Special_Untermenü = False

        if A == 4:
            pygame.draw.rect(screen, RED, [5, 345, 210, 110], 2)
            Item_Untermenü = True
        else:
            Item_Untermenü = False

        pygame.draw.rect(screen, BLACK, [10, 20, 200, 100], 100)  # Quadrat für Attack
        pygame.draw.circle(screen, GREEN, (85, 33), 10, 10)  # für +
        pygame.draw.circle(screen, RED, (100, 33), 10, 10)  # für -
        pygame.draw.rect(screen, BLACK, [10, 130, 200, 100], 100)  # Quadrat für Defend
        pygame.draw.rect(screen, BLACK, [10, 240, 200, 100], 100)  # Quadrat für Special
        pygame.draw.rect(screen, BLACK, [10, 350, 200, 100], 100)  # Quadrat für Item
        # Text darstellung
        screen.blit(Attack_text, (10, 20))
        screen.blit(Attack_Add, (80, 20))
        screen.blit(Attack_Sub, (95, 25))
        screen.blit(Defense_text, (10, 130))
        screen.blit(Special_text, (10, 240))
        screen.blit(Item_text, (10, 350))

        Player_Input_ALT = False  # Wichig! Damit A und B zurückgesetzt werden, wenn man die Stage wechselt.

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
    print(Stage1)
    # print(Player_Input_DOWN)
    # print(Player_Input_UP)
    # print (Key_pressed)
    # print(Player_Input_ALT)
    # print (B)
    # print (darstellreihenfolge())
    Frames.tick(60)
