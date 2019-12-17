import pygame
from pygame.locals import *
import time

pygame.init()

fenetre = pygame.display.set_mode((1280, 720), RESIZABLE)    #créé une fenetre de 640*480px

fond = pygame.image.load("backgroundUndertale.jpg").convert()    #import "background.png" en tant que "fond"
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
Player_Anim_Droite = [Player_Anim_Droite1,Player_Anim_Droite2,Player_Anim_Droite3,Player_Anim_Droite4,Player_Anim_Droite5,Player_Anim_Droite6]

Player_Anim_Gauche1 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche01.png").convert_alpha()
Player_Anim_Gauche2 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche02.png").convert_alpha()
Player_Anim_Gauche3 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche03.png").convert_alpha()
Player_Anim_Gauche4 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche04.png").convert_alpha()
Player_Anim_Gauche5 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche05.png").convert_alpha()
Player_Anim_Gauche6 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche06.png").convert_alpha()
Player_Anim_Gauche = [Player_Anim_Gauche1,Player_Anim_Gauche2,Player_Anim_Gauche3,Player_Anim_Gauche4,Player_Anim_Gauche5,Player_Anim_Gauche6]

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
        if event.type == QUIT:
            Continue = 0

        if event.type == KEYDOWN:

            if event.key == K_LEFT:
                for i in range(len(Player_Anim_Gauche)):
                    print (i)
                    Player = Player_Anim_Gauche[i]
                    pos_Player = pos_Player.move(-10,0)
                    time.sleep(0.05)
                    fenetre.blit(fond,(0,0))
                    fenetre.blit(Player,pos_Player)
                    pygame.display.flip()
                    time.sleep(0.001)                
                Player = Player_gauche

            elif event.key == K_RIGHT:

                for i in range(len(Player_Anim_Droite)):
                    print (i)
                    Player = Player_Anim_Droite[i]
                    pos_Player = pos_Player.move(10,0)
                    time.sleep(0.05)
                    fenetre.blit(fond,(0,0))
                    fenetre.blit(Player,pos_Player)
                    pygame.display.flip()
                    time.sleep(0.001)
                Player = Player_droite
                

            if event.key == K_UP:

                for i in range(len(Player_Anim_Haut)):
                    print (i)
                    Player = Player_Anim_Haut[i]
                    pos_Player = pos_Player.move(0,-10)
                    time.sleep(0.05)
                    fenetre.blit(fond,(0,0))
                    fenetre.blit(Player,pos_Player)
                    pygame.display.flip()
                    time.sleep(0.001)
                Player = Player_haut


            elif event.key == K_DOWN:
               Player = Player_Anim_Bas[i]
               pos_Player = pos_Player.move(0,2)
               i +=1
               if i == len(Player_Anim_Bas):
                   i = 0
    
        if event.type == KEYUP:
            if event.key == K_LEFT:
                i = 0
            elif event.key == K_RIGHT:
                i = 0
            elif event.key == K_UP:
                i = 0
            elif event.key == K_DOWN:
                i = 0
    fenetre.blit(fond,(0,0))
    fenetre.blit(Player,pos_Player)
    pygame.display.flip()

pygame.quit()