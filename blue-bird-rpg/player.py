import pygame
from constantes import *

pygame.init()

class Player(pygame.sprite.Sprite):
    spritesheet = sprites_celeste
    sequences = [(0,7,True),(8,15,True), (16,27,True), (28,39,True)]
        #            bas        haut        gauche         droite

    def __init__(self, controls, pos, pos_background):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()  #super est la superclasse Pygame.sprite.Sprite
        self.controls = controls
        # pos = data_map[self.game.room_name][4]
        self.image = Player.spritesheet.subsurface(pygame.Rect(0, 0, 128, 128)) #surface de l'image, sur le spritesheet
        self.rect = pygame.Rect(0,0,42,80)
        self.rect.topleft = (pos[0]+pos_background[0], pos[1]+pos_background[1])
        self.rect_pieds = pygame.Rect(self.rect[0]+5, self.rect[1]+70, self.rect[2]-10, self.rect[3]-70)    #rect des pieds de Celeste, pour les colision de murs
        # self.pos_img = (pos[0]+pos_background[0], pos[1]+pos_background[1]) #position de l'image, en attendant de la reduire
        self.pos_img = (self.rect[0]-37,self.rect[1]-22)    #position de l'image, par rapport  à la hitbox
        self.numeroSequence = 0 #numero de la sequence d'images utilisée
        self.numeroImage = 0    #numero de l'image utilisée
        self.sens = "down"   #orientation du personnage, pour ajuster la hitbox

        self.deltaTime = 0  #temps ecoulé en ms depuis la derniere MAJ de l'image du personnage
        self.vitesse = int(round(100/FPS))  #vitesse de deplacement du sprite

        self.move_key = []
        
    def update(self,time, keys):
        self.deltaTime = self.deltaTime + time
        if keys[pygame.K_LSHIFT]:
            sprite_time = 30
        else:
            sprite_time = 40
        if self.deltaTime >= sprite_time:   #depuis le dernier changement de sprite
            self.deltaTime = 0
            self.move_key_last = self.move_key
            self.move_key = [keys[self.controls["key_up"]], keys[self.controls["key_down"]], keys[self.controls["key_left"]], keys[self.controls["key_right"]]]

            if self.move_key_last == self.move_key and self.move_key != [0,0,0,0]:
                
                self.numeroImage = self.numeroImage + 1 #passage à l'image suivante

                if self.numeroImage > Player.sequences[self.numeroSequence][1]:
                    if Player.sequences[self.numeroSequence][2]:
                        self.numeroImage = Player.sequences[self.numeroSequence][0]
                    else:
                        self.numeroImage -= 1
                        
            else:
                self.numeroImage = Player.sequences[self.numeroSequence][0]

            n = self.numeroImage
            self.image = Player.spritesheet.subsurface(pygame.Rect(n%10*128,n//10*128,128,128))

