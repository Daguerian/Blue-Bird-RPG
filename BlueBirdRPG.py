import pygame
from pygame.locals import *
import time

pygame.init()

fenetre = pygame.display.set_mode((640, 480), RESIZABLE)    #créé une fenetre de 640*480px

fond = pygame.image.load("ChambreCelest.jpg").convert()    #import "background.png" en tant que "fond"
fond = pygame.transform.scale(fond,(640,480))

Player_bas = pygame.image.load("Sprites_Personnages\Celeste\Celeste_Marche_Bas0.png")#.convert()

Player_haut = pygame.image.load("Sprites_Personnages\Celeste\Celeste_Marche_Haut0.png")#.convert()

Player_droite = pygame.image.load("Sprites_Personnages\Celeste\Celeste_Marche_Droite00.png")#.convert()

Player_gauche = pygame.image.load("Sprites_Personnages\Celeste\Celeste_Marche_Gauche00.png")#.convert()

# Player_pos_x = 50
# Player_pos_y = 50

fenetre.blit(fond, (0,0))   #colle "fond" sur la fenetre à 0,0
Player = Player_bas #Par defaut
pos_Player = Player.get_rect()  #Recupere les coordonnées de Player (par defaut 0,0)
fenetre.blit(Player,pos_Player) 
pygame.display.flip()   #Rafraichissement de l'ecran

pygame.key.set_repeat(1, 30)
Continue = 1
while Continue:
    time.sleep(0.05)

    for event in pygame.event.get():
        if event.type == QUIT:
            Continue = 0

        if event.type == KEYDOWN:

            if event.key == K_LEFT:
                Player = Player_gauche
                pos_Player = pos_Player.move(-5,0)

            elif event.key == K_RIGHT:
                Player = Player_droite
                pos_Player = pos_Player.move(5,0)

            if event.key == K_UP:
                Player = Player_haut
                pos_Player = pos_Player.move(0,-5)

            elif event.key == K_DOWN:
                Player = Player_bas
                pos_Player = pos_Player.move(0,5)
    
        # elif event.type == KEYUP:
        #     if event.key == K_LEFT:
        #         Player = Player_gauche
        #     elif event.key == K_RIGHT:
        #         Player = Player_droite
        #     elif event.key == K_UP:
        #         Player = Player_haut
        #     elif event.key == K_DOWN:
        #         Player = Player_bas

    fenetre.blit(fond,(0,0))
    fenetre.blit(Player,pos_Player)
    pygame.display.flip()

pygame.quit()