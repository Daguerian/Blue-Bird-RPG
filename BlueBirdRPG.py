
#-*-coding python3.7-*-
#
# Structure principale du jeu
#
import pygame
from pygame.locals import *
import time

Taille_Fenetre_Defaut = (1280,720)
pygame.init()
fenetre = pygame.display.set_mode((Taille_Fenetre_Defaut))
from Constantes import *   #Fichier Constantes.py
from Classes import *      #Fichier Classes.py

### Initialisation Pygame ###
pygame.display.set_icon(Icon)
pygame.display.set_caption(Title)   #nomme la fenetre, issue de {}Constantes
pygame.key.set_repeat(1, 30)    #Repetition touche restée enfoncée & latence de sa detection
Continue = 1
i = 0

while Continue:
    pygame.time.Clock().tick(30)    #Limite la boucles à 30x/sec
    Continue_Accueil = 1

    Background_Accueil = pygame.transform.scale(Background_Accueil,Taille_Fenetre_Defaut)
    fenetre.blit(Background_Accueil, (0,0))
    pygame.display.flip()
    
    while Continue_Accueil:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:   #Quitte le jeu
                Continue_Game = 0
                Continue_Accueil = 0
                Continue = 0

            elif event.type == KEYDOWN:
                if event.key == K_t:    #Tests
                    background = background()
                    print(background.img.get_rect())
                    print ("Pos: ", background.pos)


                if event.key == K_RETURN: #Lancement à la touche Entrée
                    background = background() #charge background.__init__
                    Player = Player()
                    fenetre.blit(background.img, (background.pos))   #colle "ChambreCeleste" sur la fenetre à 0,0 (background)
                    Player.pos = Player.sprite.get_rect()
                    Player.pos = Player.pos.move((Player.pos[0]+background.pos[0],Player.pos[2]+background.pos[1]))
                    fenetre.blit(Player.sprite,Player.pos) 
                    pygame.display.flip()   #Rafraichissement de l'ecran
                    Continue_Game = 1
                    Continue_Accueil = 0

    while Continue_Game:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:   #Quitte le jeu
                Continue_Game = 0

            elif event.type == KEYDOWN or KEYUP:
                try:
                    Player.deplacement(event.type,event.key, Player)
                except:
                    print ("//")
                    time.sleep(0.1)

            fenetre.blit(background.img,background.pos)
            fenetre.blit(Player.sprite,Player.pos)
            # print (Player.sprite)
            pygame.display.flip()
            # print (Player.sprite.get_rect())


pygame.quit()