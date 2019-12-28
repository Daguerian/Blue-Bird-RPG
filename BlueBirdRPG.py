
#-*-coding python3.7-*-
#
# Structure principale du jeu
#
import pygame
from pygame.locals import *
import time
from Classes import *      #Fichier Classes.py
from Constantes import *   #Fichier Constantes.py

### Initialisation Pygame ###
pygame.init()
fenetre = pygame.display.set_mode(SizeFenetre, RESIZABLE)    #créé une fenetre de taille definié dans {}Constantes
# Icon = pygame.image.load(Icon_Image)
# pygame.display.set_icon(Icon)
pygame.display.set_caption(Title)
pygame.time.Clock().tick(30)    #Limite les boucles à 30x/sec

fond = pygame.image.load(background_img).convert()    #import "background.png" en tant que "fond"
# fond = pygame.transform.scale(fond,(640,480))



# Player_pos_x = 50
# Player_pos_y = 50

fenetre.blit(fond, (0,0))   #colle "fond" sur la fenetre à 0,0
Player = Player_bas #Par defaut
pos_Player = (265,155)
fenetre.blit(Player,pos_Player) 
pygame.display.flip()   #Rafraichissement de l'ecran
pos_Player = Player.get_rect()  #Recupere les coordonnées de Player (par defaut 0,0)

pygame.key.set_repeat(1, 30)
Continue = 1
i = 0

while Continue:
    time.sleep(0.05)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            Continue = 0

        if event.type == KEYDOWN:

            if event.key == K_LEFT or event.key == K_q:
                if i >= len(Player_Anim_Gauche):
                   i = 0
                if pos_Player in fond.get_size():   #plutto <= 0 ici, car gauche de l'ecran
                    print ("Le sprite depasse de l'ecran")
                Player = Player_Anim_Gauche[i]
                pos_Player = pos_Player.move(-5,0)
                i +=1
                Player_Orientation = "gauche"

            elif event.key == K_RIGHT or event.key == K_d:
                if i >= len(Player_Anim_Droite):
                   i = 0
                Player = Player_Anim_Droite[i]
                pos_Player = pos_Player.move(5,0)
                i +=1
                Player_Orientation = "droite"
                

            if event.key == K_UP or event.key == K_z:
                if i >= len(Player_Anim_Haut):
                   i = 0
                Player = Player_Anim_Haut[i]
                pos_Player = pos_Player.move(0,-5)
                i +=1
                Player_Orientation = "haut"


            elif event.key == K_DOWN or event.key == K_s:
               if i >= len(Player_Anim_Bas):
                   i = 0
               Player = Player_Anim_Bas[i]
               pos_Player = pos_Player.move(0,5)
               i +=1
               Player_Orientation = "bas"
            elif event.key == K_g:
                pass
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_q:
                i = 0
                Player = Player_gauche
            elif event.key == K_RIGHT or event.key == K_d:
                i = 0
                Player = Player_droite 
            elif event.key == K_UP or event.key == K_z:
                i = 0
                Player = Player_haut
            elif event.key == K_DOWN or event.key == K_s:
                i = 0
                Player = Player_bas

    fenetre.blit(fond,(0,0))
    fenetre.blit(Player,pos_Player)
    pygame.display.flip()
    print (pos_Player)


pygame.quit()