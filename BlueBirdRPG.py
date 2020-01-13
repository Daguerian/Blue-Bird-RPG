
#-*-coding python3.7-*-
#
# Structure principale du jeu
#
import pygame
from pygame.locals import *
import time

Size_Window = (800,600)
pygame.init()
fenetre = pygame.display.set_mode((Size_Window),RESIZABLE)    #créé une fenetre de taille definié dans {}Constantes
from Classes import *      #Fichier Classes.py
from Constantes import *   #Fichier Constantes.py

### Initialisation Pygame ###
pygame.display.set_icon(Icon)
pygame.display.set_caption(Title)   #nomme la fenetre, issue de {}Constantes

i = 0



# Player_pos_x = 50
# Player_pos_y = 50


pygame.key.set_repeat(1, 30)    #Repetition touche restée enfoncée & latence de sa detection
Continue = 1
i = 0

while Continue:
    pygame.time.Clock().tick(30)    #Limite la boucles à 30x/sec
    # Continue_Game = 1
    Continue_Accueil = 1

    Background_Accueil = pygame.transform.scale(Background_Accueil,(1280,720))
    fenetre.blit(Background_Accueil, (0,0))
    pygame.display.flip()
    
    while Continue_Accueil:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == VIDEORESIZE:
                x_Accueil, y_Accueil, L_Accueil, w_Accueil = Background_Accueil.get_rect()
                x_fenetre,y_fenetre,L_fenetre,w_fenetre = fenetre.get_rect()
                Background_Accueil = pygame.transform.scale(Background_Accueil,(w_fenetre,L_fenetre))
                fenetre.blit(Background_Accueil,(0,0))
                #move des boutons
                pygame.display.flip()

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:   #Quitte le jeu
                Continue_Game = 0
                Continue_Accueil = 0
                Continue = 0

            elif event.type == KEYDOWN:
                if event.key == K_t:    #Tests
                    background = ChambreCeleste
                    x_background,y_background,L_background,w_background = background.get_rect() #Length -> longueur(y) | width -> Largeur(x)
                    print ("x =",x_background)
                    print ("y =",y_background)
                    print ("L =",L_background)
                    print ("w =",w_background)

                if event.key == K_RETURN: #Lancement à la touche Entrée
                    background = ChambreCeleste #Set du background
                    x_background,y_background,L_background,w_background = background.get_rect() #Length -> longueur(y) | width -> Largeur(x)
                    x_fenetre,y_fenetre,L_fenetre,w_fenetre = fenetre.get_rect()
                    x_background = w_fenetre/2 - w_background/2
                    y_background = L_fenetre/2 - L_background/2
                    fenetre.blit(background, (x_background,y_background))   #colle "ChambreCeleste" sur la fenetre à 0,0 (background)
                    # background = pygame.transform.scale(background,(640,480))
                    Player = Celeste_bas #Sprite par defaut
                    pos_Player = Player.get_rect()
                    pos_Player = pos_Player.move((x_Player+x_background,y_Player+y_background))
                    # pos_Player = (265,155)  #set le position du joueur, plas tard stockée via un point de sauvegarde
                    fenetre.blit(Player,pos_Player) 
                    pygame.display.flip()   #Rafraichissement de l'ecran
                    Continue_Game = 1
                    Continue_Accueil = 0

    while Continue_Game:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:   #Quitte le jeu
                Continue_Game = 0
                

            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_q:
                    i = 0
                    Player = Celeste_gauche
                elif event.key == K_RIGHT or event.key == K_d:
                    i = 0
                    Player = Celeste_droite 
                elif event.key == K_UP or event.key == K_z:
                    i = 0
                    Player = Celeste_haut
                elif event.key == K_DOWN or event.key == K_s:
                    i = 0
                    Player = Celeste_bas

            elif event.type == KEYDOWN:
                   
                if event.key == K_LEFT or event.key == K_q:
                    if i >= len(Celeste_Anim_Gauche):
                        i = 0
                    if pos_Player in background.get_size():   #plutot <= 0 ici, car gauche de l'ecran
                        print ("Le sprite depasse de l'ecran")
                    Player = Celeste_Anim_Gauche[i]
                    pos_Player = pos_Player.move(-5,0)
                    i +=1
                    # Player_Orientation = "gauche"

                elif event.key == K_RIGHT or event.key == K_d:
                    if i >= len(Celeste_Anim_Droite):
                        i = 0
                    Player = Celeste_Anim_Droite[i]
                    pos_Player = pos_Player.move(5,0)
                    i +=1
                    # Player_Orientation = "droite"
                    

                if event.key == K_UP or event.key == K_z:
                    if i >= len(Celeste_Anim_Haut):
                        i = 0
                    Player = Celeste_Anim_Haut[i]
                    pos_Player = pos_Player.move(0,-5)
                    i +=1
                    # Player_Orientation = "haut"


                elif event.key == K_DOWN or event.key == K_s:
                    if i >= len(Celeste_Anim_Bas):
                        i = 0
                    Player = Celeste_Anim_Bas[i]
                    pos_Player = pos_Player.move(0,5)
                    i +=1
                    # Player_Orientation = "bas"
                   
            fenetre.blit(background,(x_background,y_background))
            fenetre.blit(Player,(pos_Player))
            pygame.display.flip()
            print (Player.get_rect())


pygame.quit()