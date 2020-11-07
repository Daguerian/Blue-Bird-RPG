from os import listdir
import json
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
font_dialogues = pygame.font.SysFont('Arial', 24, italic=False)     #texte des boits de dialogues
font_dialogues_boutons = pygame.font.SysFont('Arial', 16, italic=False)     #texte des boutons des boites de dialogues

#Main menu
main_title = "Blue Bird"
main_undertitle = "beta"
main_menu_background = pygame.image.load("data/main_menu/background.jpeg").convert_alpha()
main_menu_background = pygame.transform.scale(main_menu_background, (window_size))

#sprites
try:
    sprites_celeste = pygame.image.load("data/sprites/celeste.png").convert_alpha()
except:
    print("!!! impossible de charger tous les sprites")
    exit()

#Game
FPS = 60

data_map = {}
def import_map(nom_map):    #fonction d'importation de map
    liste_maps = listdir("data/levels/")    #liste les maps disponibles
    if nom_map in liste_maps:
        try:    #importe des parametres du fichier map_settings.json, doit être fait avant l'ajout
                #au dico car le tuple de la map (dans le dico) n'est pas modifiable
            with open(f"data/levels/{nom_map}/map_settings.json", "r") as data:
                settings = json.load(data)
                scrollable = settings["scrollable"]
                spawn_pos = settings["spawn_pos"]

            data_map[nom_map] = (   #importe dans le dictionnaire, les images & settings de la map
                pygame.image.load(f"data/levels/{nom_map}/background.png").convert_alpha(), #background
                pygame.image.load(f"data/levels/{nom_map}/hitbox.png").convert_alpha(),     #hitbox
                [], #liste des aboves_sprites
                scrollable,     #settings["scrollable"],
                spawn_pos       #settings["spawn_player"]
            )
            for filename in listdir(f"data/levels/{nom_map}"):  #check, et importation des aboves_sprites dans la liste crée au dessus
                if filename.startswith("above_sprite_"):   #syntaxe fichier: above_sprite_42.png
                    image = pygame.image.load(f"data/levels/{nom_map}/{filename}").convert_alpha()
                    data_map[nom_map][2].append(image)

            print(f"Map '{nom_map}' chargée avec succes")
            return data_map
        except Exception as err:
            print(f"!!! Erreur lors du chargement de '{nom_map}':")
            print(f"    {err}")
    else:
        print(f"{nom_map} n'existe pas dans les niveaux existants")

import_map("chambre_celeste")
import_map("sdb_chambre_celeste")
import_map("test")
import_map('re-test')

# print(data_map)