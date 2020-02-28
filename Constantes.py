import pygame
from pygame.locals import *

# Constantes du jeu
pygame.init()
SizeFenetre = (1280,720)
Title = ("Blue Bird RPG")   #Nom de la fenetre
Icon = pygame.image.load("Logo.png").convert_alpha()

compteur_sprite = 3
# Saves
x_Player = 265
y_Player = 155

# Backgrounds
Background_Accueil = pygame.image.load("Background_Accueil.png")

ChambreCeleste = pygame.image.load("ChambreCeleste.jpg")#.convert_alpha()
# Vaisseau_Hall = pygame.image.load("/").convert_alpha()

# Sprites
Celeste_bas = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas0.png").convert_alpha()
Celeste_haut = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut0.png").convert_alpha()
Celeste_droite = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite00.png").convert_alpha()
Celeste_gauche = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche00.png").convert_alpha()
# Celeste_dico = {"haut":"Celeste_haut","bas":Celeste_bas,"gauche":Celeste_gauche,"droite":Celeste_droite}

# Celeste_Anim_Bas1 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas1.png").convert_alpha()
# Celeste_Anim_Bas2 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas2.png").convert_alpha()
# Celeste_Anim_Bas3 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas3.png").convert_alpha()
# Celeste_Anim_Bas4 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas4.png").convert_alpha()
# Celeste_Anim_Bas5 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas5.png").convert_alpha()
# Celeste_Anim_Bas6 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas6.png").convert_alpha()
# Celeste_Anim_Bas = [Celeste_Anim_Bas1,Celeste_Anim_Bas2,Celeste_Anim_Bas3,Celeste_Anim_Bas4,Celeste_Anim_Bas5,Celeste_Anim_Bas6]

Celeste_Anim_Bas = []
Celeste_Anim_Bas.append(pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas1.png").convert_alpha())
Celeste_Anim_Bas.append(pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas2.png").convert_alpha())
Celeste_Anim_Bas.append(pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas3.png").convert_alpha())
Celeste_Anim_Bas.append(pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas4.png").convert_alpha())
Celeste_Anim_Bas.append(pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas5.png").convert_alpha())
Celeste_Anim_Bas.append(pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Bas6.png").convert_alpha())



Celeste_Anim_Haut1 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut1.png").convert_alpha()
Celeste_Anim_Haut2 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut2.png").convert_alpha()
Celeste_Anim_Haut3 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut3.png").convert_alpha()
Celeste_Anim_Haut4 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut4.png").convert_alpha()
Celeste_Anim_Haut5 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut5.png").convert_alpha()
Celeste_Anim_Haut6 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Haut6.png").convert_alpha()
Celeste_Anim_Haut = [Celeste_Anim_Haut1,Celeste_Anim_Haut2,Celeste_Anim_Haut3,Celeste_Anim_Haut4,Celeste_Anim_Haut5,Celeste_Anim_Haut6]

Celeste_Anim_Droite1 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite01.png").convert_alpha()
Celeste_Anim_Droite2 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite02.png").convert_alpha()
Celeste_Anim_Droite3 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite03.png").convert_alpha()
Celeste_Anim_Droite4 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite04.png").convert_alpha()
Celeste_Anim_Droite5 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite05.png").convert_alpha()
Celeste_Anim_Droite6 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite06.png").convert_alpha()
Celeste_Anim_Droite7 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite07.png").convert_alpha()
Celeste_Anim_Droite8 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite08.png").convert_alpha()
Celeste_Anim_Droite9 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite09.png").convert_alpha()
Celeste_Anim_Droite10 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite10.png").convert_alpha()
Celeste_Anim_Droite11 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Droite11.png").convert_alpha()
Celeste_Anim_Droite = [Celeste_Anim_Droite1,Celeste_Anim_Droite2,Celeste_Anim_Droite3,Celeste_Anim_Droite4,Celeste_Anim_Droite5,
Celeste_Anim_Droite6,Celeste_Anim_Droite7,Celeste_Anim_Droite8,Celeste_Anim_Droite9,Celeste_Anim_Droite10,Celeste_Anim_Droite11]

Celeste_Anim_Gauche1 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche01.png").convert_alpha()
Celeste_Anim_Gauche2 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche02.png").convert_alpha()
Celeste_Anim_Gauche3 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche03.png").convert_alpha()
Celeste_Anim_Gauche4 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche04.png").convert_alpha()
Celeste_Anim_Gauche5 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche05.png").convert_alpha()
Celeste_Anim_Gauche6 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche06.png").convert_alpha()
Celeste_Anim_Gauche7 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche07.png").convert_alpha()
Celeste_Anim_Gauche8 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche08.png").convert_alpha()
Celeste_Anim_Gauche9 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche09.png").convert_alpha()
Celeste_Anim_Gauche10 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche10.png").convert_alpha()
Celeste_Anim_Gauche11 = pygame.image.load("Sprites_Personnages/Celeste/Celeste_Marche_Gauche11.png").convert_alpha()
Celeste_Anim_Gauche = [Celeste_Anim_Gauche1,Celeste_Anim_Gauche2,Celeste_Anim_Gauche3,Celeste_Anim_Gauche4,Celeste_Anim_Gauche5,
Celeste_Anim_Gauche6,Celeste_Anim_Gauche7,Celeste_Anim_Gauche8,Celeste_Anim_Gauche9,Celeste_Anim_Gauche10,Celeste_Anim_Gauche11]

Celeste_dico = {"haut":Celeste_Anim_Haut,"bas":Celeste_Anim_Bas,"gauche":Celeste_Anim_Gauche,"droite":Celeste_Anim_Droite}