import pygame
from pygame.locals import *
from constantes import *
import json
pygame.init()
pygame.font.init()

class Status():
    def __init__(self):
        self.on_app = 1
        self.on_main_menu = 1
        self.on_settings = 0
        self.on_game = 0
status = Status()

class Main_Menu():
    def __init__(self, window):
        self.window = window
        color_1 = color_2 = color_3 = (67,67,67)    #gris foncé 
        self.bouton1 = pygame.draw.rect(window, (color_1), (515, 300, 250, 50))
        self.bouton2 = pygame.draw.rect(window, (color_2), (515, 370, 250, 50))
        self.bouton3 = pygame.draw.rect(window, (color_3), (515, 440, 250, 50))
        self.text_title = font_title.render(main_title, True, (255,0,255))
        self.text_undertitle = font_undertitle.render(main_undertitle, True, (255,255,255))
        self.text_play = font.render("Jouer", True, (255,255,255))
        self.text_options = font.render("Options", True, (255,255,255))
        self.text_quit = font.render("Quitter", True, (255,255,255))
        self.update()

    def update(self):
        mousePressed = pygame.mouse.get_pressed()
        x,y = pygame.mouse.get_pos()
        
        
        if self.bouton1.collidepoint(x,y):  #souris dans la hitbox de bouton1
            color_1 = (100,100,100)
            if mousePressed[0]: # 0 - clic Left
                print ("[play button]")
                status.on_main_menu = 0
                status.on_game = 1
                opacity = 0
                for i in range(25):
                    fondu = pygame.Surface((1280,720))
                    fondu.set_alpha(opacity)
                    fondu.fill((0,0,0))
                    self.window.blit(fondu, (0,0))
                    opacity += 10
                    pygame.time.wait(25)
                    pygame.display.flip()
        else:
            color_1 = (67,67,67)

        if self.bouton2.collidepoint(x,y):  #action Bouton 2 - Option
            color_2 = (100,100,100)
            if mousePressed[0]: # 0 - clic Left
                print ("[settings button]")
                # status.on_main_menu = 0
                # status.on_settings = 1

        else:
            color_2 = (67,67,67)

        if self.bouton3.collidepoint(x,y):  #action Bouton 3 - Quit
            color_3 = (100,100,100)
            if mousePressed[0]: # 0 - clic Left
                print ("[exit button]")
                status.on_main_menu = 0
                status.on_app = 0

        else:
            color_3 = (67,67,67)

        if status.on_main_menu: #pour eviter de gacher la fin du fondu, lors d'un clic
            self.window.blit(main_menu_background, (0,0))
            self.bouton1 = pygame.draw.rect(self.window, (color_1), (515, 300, 250, 50))
            self.bouton2 = pygame.draw.rect(self.window, (color_2), (515, 370, 250, 50))
            self.bouton3 = pygame.draw.rect(self.window, (color_3), (515, 440, 250, 50))

            self.window.blit(self.text_play,((self.bouton1[0]+get_lefttop(self.text_play,self.bouton1,2)[0]), (300+get_lefttop(self.text_play,self.bouton1,2)[1])))
            self.window.blit(self.text_options,((self.bouton2[0]+get_lefttop(self.text_options,self.bouton2,2)[0]) ,370+get_lefttop(self.text_options,self.bouton2,2)[1]))
            self.window.blit(self.text_quit, ((self.bouton3[0]+get_lefttop(self.text_quit,self.bouton3,2)[0]),(440+get_lefttop(self.text_quit,self.bouton3,2)[1])))
            self.window.blit(self.text_title,(get_lefttop(self.text_title,self.window,0)[0],100))
            self.window.blit(self.text_undertitle, (800,180))   #beta

class Settings():
    def __init__(self):
        self.key_up = 122
        self.key_down = 115
        self.key_left = 113
        self.key_right = 100
        self.key_debug = 119
        print(self.key_up)
        print(self.key_down)
        print(self.key_left)
        print(self.key_right)
        print(self.key_debug)
        print("Settings chargés")

def get_lefttop(frontbox, backbox, AlreadyRect):    #frontbox: texte par exemple, backbox: bouton par exemple
    if AlreadyRect == 0:    # 0 = aucun deja rect
        rect1 = frontbox.get_rect()
        rect2 = backbox.get_rect()
    elif AlreadyRect == 1:    # 1 = frontbox deja rect
        rect1 = frontbox
        rect2 = backbox.get_rect()
    elif AlreadyRect ==2:   # 2 = backbox deja rect
        rect1 = frontbox.get_rect()
        rect2 = backbox
    elif AlreadyRect == 3:  # 3 = frontbox et backbox deja rect
        rect1 = frontbox
        rect2 = backbox
    
    point = ((rect2[2]/2 - rect1[2]/2), rect2[3]/2 - rect1[3]/2)
    return point

### Game ###
class Game():
    def __init__(self, window):
        self.rect_background = None
        self.window = window
        self.sauvegarde = None
        try:
            with open("data/sauvegarde.save","r") as data:
                self.sauvegarde = data.read()
                self.sauvegarde = eval(self.sauvegarde) #convert str vers dict
                print ("Sauvegarde chargée")


        except FileNotFoundError:
            print("Sauvegarde non trouvée")
            self.text_reset_save_exc = font.render("Sauvegarde non trouvée", True,(255,255,255))
            self.text_reset_save = font.render("Voulez-vous en créer une nouvelle ?", True,(255,255,255))
            self.update_reset_sauvegarde()
        except:
            self.text_reset_save_exc = font.render("Impossible de charger la sauvegarde", True,(255,255,255))
            self.text_reset_save = font.render("Voulez-vous en créer une nouvelle ?", True,(255,255,255))
            self.update_reset_sauvegarde()

        if self.sauvegarde:
            level = self.sauvegarde["level"]
            if level in data_map:
                try:
                    self.room_name = level   #str du nom de la map
                    self.background = data_map[self.room_name][0]    #recupere le background selon la map demandée
                    self.pos_background = get_lefttop(self.background, window, 0)
                    self.above_sprite_list = data_map[level][2]
                    self.above_sprite = None
                    self.hitbox = data_map[level][1]
                except:
                    print ("impossible de charger le background")
                    status.on_game = 0
            else:
                print("impossible de trouver le background")
                status.on_game = 0

    def update_reset_sauvegarde(self):  #fenetre en cas de sauvegarde non chargée
        color_oui = color_non = (67,67,67)
        self.bouton_oui = pygame.draw.rect(self.window, (color_oui), (340,370,250,50))
        self.bouton_non = pygame.draw.rect(self.window, (color_non), (690,370,250,50))
        while True:
            pygame.time.Clock().tick(30)
            mousePressed = pygame.mouse.get_pressed()
            x,y = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    status.on_game = 0


            if self.bouton_oui.collidepoint(x,y): #Bouton Oui
                color_oui = (100,100,100)
                if mousePressed[0]: #0 - clic Left
                    self.reset_sauvegarde()
                    break
            else:
                color_oui = (67,67,67)
            
            if self.bouton_non.collidepoint(x,y): #Bouton Non
                color_non = (100,100,100)
                if mousePressed[0]:
                    status.on_game = 0
                    break
            else: 
                color_non = (67,67,67)

            self.window.blit(main_menu_background, (0,0))
            self.window.blit(self.text_reset_save_exc, (get_lefttop(self.text_reset_save_exc,self.window,0)[0],100))
            self.window.blit(self.text_reset_save, (get_lefttop(self.text_reset_save,self.window,0)[0],200))

            text_oui = font.render("Oui", True, (255,255,255))
            self.bouton_oui = pygame.draw.rect(self.window, (color_oui), (340,370,250,50))
            self.window.blit(text_oui, (340+125-text_oui.get_rect()[2]/2, 370+25-text_oui.get_rect()[3]/2))

            text_non = font.render("Non", True, (255,255,255))
            self.bouton_non = pygame.draw.rect(self.window, (color_non), (690,370,250,50))
            self.window.blit(text_non, (690+125-text_non.get_rect()[2]/2, 370+25-text_non.get_rect()[3]/2))
            pygame.display.flip()

    def reset_sauvegarde(self):
        self.sauvegarde = {}
        self.sauvegarde["level"] = ("chambre_celeste")
        try:
            with open("data/sauvegarde.save","w") as data:
                # json.dump(self.sauvegarde, data, indent=4)
                data.write(str(self.sauvegarde))
                print("fichier de sauvegarde créé")
                
        except:
            # status.on_game = 0
            print ("/!\ impossible de créer le fichier de sauvegarde")
        

class Player(pygame.sprite.Sprite):
    spritesheet = sprites_celeste
    sequences = [(0,7,True),(8,15,True), (16,27,True), (28,39,True)]
        #            bas        haut        gauche         droite

    def __init__(self, game):
        self.settings = Settings()
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        pos = data_map[self.game.room_name][4]
        self.image = Player.spritesheet.subsurface(pygame.Rect(0, 0, 128, 128))
        self.rect = pygame.Rect(0,0,42,80)
        self.rect.topleft = (pos[0]+self.game.pos_background[0], pos[1]+self.game.pos_background[1])
        self.rect_pieds = pygame.Rect(self.rect[0]+5, self.rect[1]+70, self.rect[2]-10, self.rect[3]-70)    #rect des pieds de Celeste, pour les colision de murs
        # self.pos_img = (pos[0]+self.game.pos_background[0], pos[1]+self.game.pos_background[1]) #position de l'image, en attendant de la reduire
        self.pos_img = (self.rect[0]-37,self.rect[1]-22)    #position de l'image, par rapport  à la hitbox
        self.numeroSequence = 0 #numero de la sequence d'images utilisée
        self.numeroImage = 0    #numero de l'image utilisée
        self.sens = "down"   #orientation du personnage, pour ajuster la hitbox

        self.deltaTime = 0  #temps ecoulé en ms depuis la derniere MAJ de l'image du personnage
        self.vitesse = int(round(100/FPS))  #vitesse de deplacement du sprite

        self.move_key = []

    def change_room(self, room, porte):
        if porte == 1:
            if room == "chambre_celeste":
                self.game.room_name = "sdb_chambre_celeste"
                self.game.above_sprite = None
                pos = (540,460)
                # self.rect[0], self.rect[1] = 580,460
            elif room == "sdb_chambre_celeste":
                self.game.room_name = "chambre_celeste"
                self.game.above_sprite = None
                pos = (920,455)

        elif room == 2:
            pass
        diff_pos_pieds = self.rect_pieds[0] - self.rect[0], self.rect_pieds[1] - self.rect[1]
        diff_pos_img = self.rect[0] - self.pos_img[0], self.rect[1] - self.pos_img[1]
        self.rect[0],self.rect[1] = (pos+self.game.pos_background)[0],(pos+self.game.pos_background)[1]
        self.rect_pieds[0], self.rect_pieds[1] = self.rect[0]+diff_pos_pieds[0], self.rect[1]+diff_pos_pieds[1]
        self.pos_img = self.rect[0]-diff_pos_img[0], self.rect[1]-diff_pos_img[1]
        self.game.background = data_map[self.game.room_name][0]
        self.game.pos_background = get_lefttop(self.game.background, self.game.window, 0)
        self.game.above_sprite_list = data_map[self.game.room_name][2]
        self.game.hitbox = data_map[self.game.room_name][1]

    def hit(self, rect, sens, pos_background):
        hit = [pygame.Color(0,0,0,0),pygame.Color(0,0,0,0)]
        pos = pos_background
        x = int(rect[0] - pos[0])
        xx = int(x + rect[2])
        y = int(rect[1] - pos[1])
        yy = int(y + rect[3])
        if sens == "up":
            hit[0] += self.game.hitbox.get_at((int(x),int(y)))  #point haut-gauche
            hit[1] += self.game.hitbox.get_at((int(xx),int(y))) #point haut-droite
        elif sens == "down":
            hit[0] += self.game.hitbox.get_at((int(x),int(yy))) #point bas-gauche
            hit[1] += self.game.hitbox.get_at((int(xx),int(yy))) #point bas-droite
        elif sens == "left":
            hit[0] += self.game.hitbox.get_at((int(x),int(y)))  #point gauche-haut
            hit[1] += self.game.hitbox.get_at((int(x),int(yy))) #ect...
        elif sens == "right":
            hit[0] += self.game.hitbox.get_at((int(xx),int(y)))
            hit[1] += self.game.hitbox.get_at((int(xx),int(yy)))
            #du 1er au 3e NON INCLUS 
        if hit[0][0:3] == (255, 255, 255) and hit[1][0:3] == (255, 255, 255):    #couleur blanche, aucun above
            self.game.above_sprite = None
            return "can_move"
        elif hit[0][0:3] == (255,0,0) and hit[1][0:3] == (255,0,0):      #couleur rouge, above 1
            self.game.above_sprite = self.game.above_sprite_list[0]
            return "can_move"
        elif hit[0][0:3] == (255,106,0) and hit[1][0:3] == (255,106,0):    #couleur orange, above 2
            self.game.above_sprite = self.game.above_sprite_list[1]
            return "can_move"
        elif hit[0][0:3] == (255,216,0) and hit[1][0:3] == (255,216,0):         #couleur jaune, above 3
            self.game.above_sprite = self.game.above_sprite_list[2]
        #Portes
        if hit[0][0:3] == (255,0,110) or hit[1][0:3] == (255,0,110):      #rose/violet, porte 1
            self.change_room(self.game.room_name, 1)
        elif (255,110,110) in hit:  # , porte 2
            pass
        # print(hit[0])
        # print(hit[1])
        
    def update(self,time, keys):
        self.deltaTime = self.deltaTime + time
        if keys[pygame.K_LSHIFT]:
            sprite_time = 30
        else:
            sprite_time = 40
        if self.deltaTime >= sprite_time:   #depuis le dernier changement de sprite
            self.deltaTime = 0
            self.move_key_last = self.move_key
            self.move_key = [keys[self.settings.key_up], keys[self.settings.key_down], keys[self.settings.key_left], keys[self.settings.key_right]]

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

    def moveRight(self):
        newrect = self.rect.move(self.vitesse,0)    #prochain rect
        newrect_pieds = self.rect_pieds.move(self.vitesse,0)
        if self.hit(newrect_pieds,"right",self.game.pos_background) == "can_move":
            self.rect = newrect
            self.rect_pieds = self.rect_pieds.move(self.vitesse,0)
            self.rect[2] = 20
            self.pos_img = (self.rect[0]-40,self.rect[1]-22)
            # self.rect = self.rect.move(self.vitesse,0)#.clamp(self.rect_background) #eventuellement sur l'image hitbox ?
            self.numeroSequence = 3
            self.move_sprite = (self.vitesse,0)
            if self.sens in ["up", "down"]:
                self.rect[0] += 11
                # self.rect_pieds[0] += 6
                # self.rect_pieds[2] -= 12
            self.sens = "right"
        else:
            pass
    def moveLeft(self):
        newrect = self.rect.move(-self.vitesse,0)
        newrect_pieds = self.rect_pieds.move(-self.vitesse,0)
        if self.hit(newrect_pieds,"left",self.game.pos_background) == "can_move":
            self.rect = newrect
            self.rect_pieds = newrect_pieds
            self.rect[2] = 20
            self.pos_img = (self.rect[0]-40,self.rect[1]-22)
            # self.rect = self.rect.move(-self.vitesse,0)#.clamp(self.rect_background)
            self.numeroSequence = 2
            self.move_sprite = (-self.vitesse,0)
            if self.sens in ["up", "down"]:
                self.rect[0] += 11
                # self.rect_pieds[0] += 6
                # self.rect_pieds[2] -= 12
            self.sens = "left"
        else:
            pass
    
    def moveUp(self):
        newrect = self.rect.move(0,-self.vitesse)
        newrect_pieds = self.rect_pieds.move(0,-self.vitesse)
        if self.hit(newrect_pieds,"up",self.game.pos_background) == "can_move":
            self.rect = newrect
            self.rect_pieds = newrect_pieds
            self.rect[2] = 42
            self.pos_img = (self.rect[0]-37,self.rect[1]-22)
            # self.rect = self.rect.move(0,-self.vitesse)#.clamp(self.rect_background)
            self.numeroSequence = 1
            self.move_sprite = (0,-self.vitesse)
            if self.sens in ["left", "right"]:
                self.rect[0] -= 11
                # self.rect_pieds[0] -= 6
                # self.rect_pieds[2] += 12
            self.sens = "up"
        else:
            pass

    def moveDown(self):
        newrect = self.rect.move(0,self.vitesse)
        newrect_pieds = self.rect_pieds.move(0,self.vitesse)
        if self.hit(newrect_pieds,"down",self.game.pos_background) == "can_move":
            self.rect = newrect
            self.rect_pieds = newrect_pieds
            self.rect[2] = 42
            self.pos_img = (self.rect[0]-37,self.rect[1]-22)
            # self.rect = self.rect.move(0,self.vitesse)#.clamp(self.rect_background)
            self.numeroSequence = 0
            self.move_sprite = (0,self.vitesse)
            if self.sens in ["left", "right"]:
                self.rect[0] -= 11
                # self.rect_pieds[0] -= 6
                # self.rect_pieds[2] += 12
            self.sens = "down"
        else:
            pass