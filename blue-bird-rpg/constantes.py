import pygame
from pygame.locals import *
pygame.init()
pygame.display.init()
pygame.font.init()

window_size = (1280,720)
window = pygame.display.set_mode(window_size)

Title = "Blue Bird RPG"
try:
    Icon = pygame.image.load("icon.png").convert_alpha()
except:
    print("! impossible de charger l'icon")

font = pygame.font.SysFont('Alef', 50, bold=False, italic=False)    #texte boutons main menu
font_title = pygame.font.SysFont('Carlito', 120, bold=True)         #texte title main menu
font_undertitle = pygame.font.SysFont('Carlito', 30, italic=True)   #texte "beta" sous le title
font_dialogues = pygame.font.SysFont('Arial', 24, italic=False)     #texte des dialogues

#Main menu
main_title = "Blue Bird"
main_undertitle = "beta"
main_menu_background = pygame.image.load("data/main_menu/background.jpeg").convert_alpha()
main_menu_background = pygame.transform.scale(main_menu_background, (window_size))

#fonds levels
try:    #chambre celeste
    chambre_celeste = pygame.image.load("data/levels/chambre_celeste/background.png").convert_alpha()
    chambre_celeste_above_1 = pygame.image.load("data/levels/chambre_celeste/above_sprite_1.png").convert_alpha()
    chambre_celeste_above_2 = pygame.image.load("data/levels/chambre_celeste/above_sprite_2.png").convert_alpha()
    chambre_celeste_hitbox = pygame.image.load("data/levels/chambre_celeste/hitbox.png").convert_alpha()
    #+ lampes/animations

except:
    print("!!! impossible de charger tous les fichiers de chambre_celeste")
    exit()

try:    #sdb celeste
    sdb_celeste = pygame.image.load("data/levels/sdb_chambre_celeste/background.png").convert_alpha()
    sdb_celeste_above_1 = pygame.image.load("data/levels/sdb_chambre_celeste/above_sprite_1.png").convert_alpha()
    sdb_celeste_above_2 = pygame.image.load("data/levels/sdb_chambre_celeste/above_sprite_2.png").convert_alpha()
    sdb_celeste_hitbox = pygame.image.load("data/levels/sdb_chambre_celeste/hitbox.png").convert_alpha()
except:
    print("!!! Impossible de charger tous les fichiers de sdb_chambre_celeste")
#sprites
try:
    sprites_celeste = pygame.image.load("data/sprites/celeste.png").convert_alpha()
except:
    print("!!! impossible de charger tous les sprites")
    exit()

#Game
FPS = 60
data_map = {}                                                                                                                     #pos joueur
         #  Nom de la salle      background           img hitbox                liste des imgs above sprite               scrollable
data_map["chambre_celeste"] = (
    chambre_celeste,    #img background
    chambre_celeste_hitbox ,    #img hitbox
    [chambre_celeste_above_1,chambre_celeste_above_2],  #liste des aboves-sprite
    False,      #scrollable
    (400, 500)  #pos spawn joueur
    )
data_map["sdb_chambre_celeste"] = (
    sdb_celeste,
    sdb_celeste_hitbox,
    [sdb_celeste_above_1, sdb_celeste_above_2],
    False,
    (540,470)
    )
