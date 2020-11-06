#/usr/bin/python3.7
#
# Structure principale du jeu
#v. dev

import pygame
from pygame.locals import *
import time
debug_mode = False
#Initialisation 
pygame.init()
from constantes import *
# window = pygame.display.set_mode(window_size)    #move {}constantes ?
from classes import *
pygame.font.init()

pygame.display.set_icon(Icon)
pygame.display.set_caption(Title)
pygame.key.set_repeat(1, 30)

last_press_debug = 0
last_press_menu = 0

while status.on_app:    #App ouverte
    pygame.time.Clock().tick(30)    # boucle 30x /s
    status.on_main_menu = 1
    main_menu = Main_Menu(window) #Init

    while status.on_main_menu:  #sur le menu principal
        pygame.time.Clock().tick(200)
        for event in pygame.event.get():    #detection des evenements
            if event.type == QUIT:  #si on quitte
                status.on_main_menu = 0
                status.on_app = 0

            if pygame.mouse.get_focused():  #
                main_menu.update()
        pygame.display.flip()   #update apres le test main_menu.update(), en cas de changement mais reste en boucle 200Hz pour reduire le lag

    while status.on_settings:   #Menu des options
        status.on_settings = 0    #quitte automatiquement, car encore innexistant
        status.on_main_menu = 1
        break

    if status.on_game:  #si bouton play, lance le chargement de sauvegarde
        game = Game(window)
        if status.on_game:  #ne lance pas si la re-création de sauvagarde a été refusée
            opacity = 250
            for i in range(25): #fondu, fond noir avec reduction de l'opacité
                fondu = pygame.Surface((1280,720))
                fondu.set_alpha(opacity)
                window.blit(game.background, (game.pos_background))
                window.blit(game.player.image, game.player.pos_img)
                fondu.fill((0,0,0))
                window.blit(fondu, (0,0))
                opacity -= 10
                pygame.time.wait(25)
                pygame.display.flip()


    while status.on_game:   #En jeu
        time = pygame.time.Clock().tick(FPS)    #pour reguler la vitesse du perso et des animations
        keys = pygame.key.get_pressed()

        last_press_debug += time
        last_press_menu += time

        if not status.game_in_menu:
            
            if keys[game.controls['key_sprint']]:   #active ou desactive le mode de sprint
                game.player.vitesse = int(round(100/FPS)) + 2
            else:
                game.player.vitesse = int(round(100/FPS))

            if keys[game.controls['key_right']]:    #controle move droite
                game.moveRight()

            elif keys[game.controls['key_left']]:   #controle move gauche
                game.moveLeft()

            elif keys[game.controls['key_up']]:     #controle move haut
                game.moveUp()

            elif keys[game.controls['key_down']]:   #controle move bas
                game.moveDown()

            if keys[game.controls['key_menu']] and last_press_menu > 150:
                last_press_menu = 0
                print("entrée menu d'interraction")
                status.game_in_menu = 1
        
        if status.game_in_menu:
            if keys[game.controls['key_menu']] and last_press_menu > 150:
                last_press_menu = 0
                print("sortie menu d'interraction")
                status.game_in_menu = 0

        #debug mode
        
        if keys[game.controls['key_debug']] and last_press_debug > 150 and debug_mode:  #cooldown avant de switch le debug mode
            debug_mode = False
            last_press_debug = 0
        elif keys[game.controls['key_debug']] and last_press_debug > 150:
            debug_mode = True
            last_press_debug = 0

        if keys[pygame.K_ESCAPE]:   #retour au menu principal avec Echap
            status.on_game = 0
        for event in pygame.event.get():    #et en essayant de quitter le jeu
            if event.type == QUIT:
                status.on_game = 0

        #update de l'ecran
        window.fill((0,0,0))    #black screen arriere plan
        window.blit(game.background, (game.pos_background)) #background de la salle

        if debug_mode:  #sous celeste, affiche les hitbox de la salle
            window.blit(game.hitbox, game.pos_background)   

        if not status.game_in_menu: #seulement hors des menus in-game (dialogue, ect)
            game.player.update(time, keys)  #animation du joueur, update du sprite
        window.blit(game.player.image, game.player.pos_img) #blit sprite Celeste

        if game.above_sprite:   #si un above-sprite est defini, l'affiche au dessus de Celeste
            window.blit(game.above_sprite, (game.pos_background))

        if debug_mode:  #au dessus de celeste, hitbox de Celeste
            pygame.draw.rect(window, (0,255,0), game.player.rect, 2)
            pygame.draw.rect(window, (255,0,0), game.player.rect_pieds, 2)
            pygame.draw.rect(window, (0,0,255), (game.player.pos_img[0], game.player.pos_img[1], game.player.image.get_rect()[2],game.player.image.get_rect()[3]), 2)

        if status.game_in_menu:
            game.dialog_box("Hey ! ceci est un teeest", "Bouton")

        pygame.display.flip()
