import pygame
from pygame.locals import *
import time

pygame.init()

fenetre = pygame.display.set_mode((1280, 720), RESIZABLE)    #créé une fenetre de 640*480px

fond = pygame.image.load("BackgroundUndertale.jpg").convert()    #import "background.png" en tant que "fond"
# fond = pygame.transform.scale(fond,(640,480))


Player_bas = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas0.png").convert_alpha()
Player_haut = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut0.png").convert_alpha()
Player_droite = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite00.png").convert_alpha()
Player_gauche = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche00.png").convert_alpha()

Player_Anim_Bas1 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas1.png").convert_alpha()
Player_Anim_Bas2 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas2.png").convert_alpha()
Player_Anim_Bas3 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas3.png").convert_alpha()
Player_Anim_Bas4 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas4.png").convert_alpha()
Player_Anim_Bas5 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas5.png").convert_alpha()
Player_Anim_Bas6 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas6.png").convert_alpha()
Player_Anim_Bas = [Player_Anim_Bas1,Player_Anim_Bas2,Player_Anim_Bas3,Player_Anim_Bas4,Player_Anim_Bas5,Player_Anim_Bas6]

Player_Anim_Haut1 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut1.png").convert_alpha()
Player_Anim_Haut2 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut2.png").convert_alpha()
Player_Anim_Haut3 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut3.png").convert_alpha()
Player_Anim_Haut4 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut4.png").convert_alpha()
Player_Anim_Haut5 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut5.png").convert_alpha()
Player_Anim_Haut6 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut6.png").convert_alpha()
Player_Anim_Haut = [Player_Anim_Haut1,Player_Anim_Haut2,Player_Anim_Haut3,Player_Anim_Haut4,Player_Anim_Haut5,Player_Anim_Haut6]

Player_Anim_Droite1 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite01.png").convert_alpha()
Player_Anim_Droite2 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite02.png").convert_alpha()
Player_Anim_Droite3 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite03.png").convert_alpha()
Player_Anim_Droite4 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite04.png").convert_alpha()
Player_Anim_Droite5 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite05.png").convert_alpha()
Player_Anim_Droite6 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite06.png").convert_alpha()
Player_Anim_Droite7 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite07.png").convert_alpha()
Player_Anim_Droite8 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite08.png").convert_alpha()
Player_Anim_Droite9 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite09.png").convert_alpha()
Player_Anim_Droite10 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite10.png").convert_alpha()
Player_Anim_Droite11 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite11.png").convert_alpha()
Player_Anim_Droite = [Player_Anim_Droite1,Player_Anim_Droite2,Player_Anim_Droite3,Player_Anim_Droite4,Player_Anim_Droite5,
Player_Anim_Droite6,Player_Anim_Droite7,Player_Anim_Droite8,Player_Anim_Droite9,Player_Anim_Droite10,Player_Anim_Droite11]

Player_Anim_Gauche1 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche01.png").convert_alpha()
Player_Anim_Gauche2 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche02.png").convert_alpha()
Player_Anim_Gauche3 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche03.png").convert_alpha()
Player_Anim_Gauche4 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche04.png").convert_alpha()
Player_Anim_Gauche5 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche05.png").convert_alpha()
Player_Anim_Gauche6 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche06.png").convert_alpha()
Player_Anim_Gauche7 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche07.png").convert_alpha()
Player_Anim_Gauche8 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche08.png").convert_alpha()
Player_Anim_Gauche9 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche09.png").convert_alpha()
Player_Anim_Gauche10 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche10.png").convert_alpha()
Player_Anim_Gauche11 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche11.png").convert_alpha()
Player_Anim_Gauche = [Player_Anim_Gauche1,Player_Anim_Gauche2,Player_Anim_Gauche3,Player_Anim_Gauche4,Player_Anim_Gauche5,
Player_Anim_Gauche6,Player_Anim_Gauche7,Player_Anim_Gauche8,Player_Anim_Gauche9,Player_Anim_Gauche10,Player_Anim_Gauche11]

# Player_pos_x = 50
# Player_pos_y = 50

fenetre.blit(fond, (0,0))   #colle "fond" sur la fenetre à 0,0
Player = Player_bas #Par defaut
pos_Player = Player.get_rect()  #Recupere les coordonnées de Player (par defaut 0,0)
fenetre.blit(Player,pos_Player) 
pygame.display.flip()   #Rafraichissement de l'ecran

pygame.key.set_repeat(1, 30)
Continue = 1
i = 0


while Continue:
    time.sleep(0.05)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            Continue = 0

        if event.type == KEYDOWN:

            if event.key == K_LEFT or event.key == ord("q"):
                if i >= len(Player_Anim_Gauche):
                   i = 0
                if pos_Player in fond.get_size():   #plutto <= 0 ici, car gauche de l'ecran
                    print ("Le sprite depasse de l'ecran")
                Player = Player_Anim_Gauche[i]
                pos_Player = pos_Player.move(-5,0)
                i +=1
                Player_Orientation = "gauche"

            elif event.key == K_RIGHT or event.key == ord("d"):
                if i >= len(Player_Anim_Droite):
                   i = 0
                Player = Player_Anim_Droite[i]
                pos_Player = pos_Player.move(5,0)
                i +=1
                Player_Orientation = "droite"
                

            if event.key == K_UP or event.key == ord("z"):
                if i >= len(Player_Anim_Haut):
                   i = 0
                Player = Player_Anim_Haut[i]
                pos_Player = pos_Player.move(0,-5)
                i +=1
                Player_Orientation = "haut"


            elif event.key == K_DOWN or event.key == ord("s"):
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


pygame.quit()