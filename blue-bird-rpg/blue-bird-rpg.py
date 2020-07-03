#/usr/bin/python3.7
#
# Structure principale du jeu

import pygame
from pygame.locals import *
import time
debug_mode = False
#Initialisation 
pygame.init()
window = pygame.display.set_mode((1280,720))    #move {}constantes ?
from classes import *
from constantes import *
pygame.font.init()

pygame.display.set_icon(Icon)
pygame.display.set_caption(Title)
pygame.key.set_repeat(1, 30)

last_press_debug = 0

while status.on_app:
    pygame.time.Clock().tick(30)    # boucle 30x /s
    settings = Settings()
    status.on_main_menu = 1
    main_menu = Main_Menu(window) #Init

    while status.on_main_menu:
        pygame.time.Clock().tick(200)
        for event in pygame.event.get():
            if event.type == QUIT:
                status.on_main_menu = 0
                status.on_app = 0

            if pygame.mouse.get_focused():
                main_menu.update()
        pygame.display.flip()
        if status.on_game:  #si bouton play, lance le chargement de sauvegarde
            game = Game(window)
            if status.on_game:  #ne lance pas si la re-création de sauvagarde a été refusée
                perso = Player(game)
                opacity = 250
                for i in range(25): #fondu, fond noir avec reduction de l'opacité
                    fondu = pygame.Surface((1280,720))
                    fondu.set_alpha(opacity)
                    window.blit(game.background, (game.pos_background))
                    window.blit(perso.image, perso.pos_img)
                    fondu.fill((0,0,0))
                    window.blit(fondu, (0,0))
                    opacity -= 10
                    pygame.time.wait(25)
                    pygame.display.flip()


    while status.on_settings:
        status.on_settings = 0    #ecran des options
        status.on_main_menu = 1
        break


    while status.on_game:
        time = pygame.time.Clock().tick(FPS)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            perso.vitesse = int(round(100/FPS)) + 2
        else:
            perso.vitesse = int(round(100/FPS))
        if keys[settings.key_right]:
            perso.moveRight()

        elif keys[settings.key_left]:
            perso.moveLeft()

        elif keys[settings.key_up]:
            perso.moveUp()

        elif keys[settings.key_down]:
            perso.moveDown()

        #debug mode
        last_press_debug += time
        if keys[settings.key_debug] and last_press_debug > 150 and debug_mode:
            debug_mode = False
            last_press_debug = 0
        elif keys[settings.key_debug] and last_press_debug > 150:
            debug_mode = True
            last_press_debug = 0

        if keys[pygame.K_ESCAPE]:
            status.on_game = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                status.on_game = 0
        # liste = [keys[pygame.K_RIGHT], keys[pygame.K_LEFT], keys[pygame.K_UP], keys[pygame.K_DOWN]]
        # print(liste)
        perso.update(time, keys)
        window.fill((0,0,0))    #black screen arriere plan
        window.blit(game.background, (game.pos_background)) #background 
        if debug_mode:  #sous celeste
            window.blit(game.hitbox, game.pos_background)
        
        window.blit(perso.image, perso.pos_img) #sprite celeste

        if game.above_sprite:   #si un above_sprite est defini
            window.blit(game.above_sprite, (game.pos_background))

        if debug_mode:  #au dessus de celeste
            pygame.draw.rect(window, (0,255,0), perso.rect, 2)
            pygame.draw.rect(window, (255,0,0), perso.rect_pieds, 2)
            pygame.draw.rect(window, (0,0,255), (perso.pos_img[0], perso.pos_img[1], perso.image.get_rect()[2],perso.image.get_rect()[3]), 2)



        pygame.display.flip()