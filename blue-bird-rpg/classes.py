import pygame
from pygame.locals import *
from constantes import *
from player import Player
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
        self.window = window
        try:    #charge la sauvegarde contenant le level et les controles, et verifie l'integrité
            with open("data/sauvegarde.json","r") as data:
                self.sauvegarde = json.load(data)
                print(f"level selectionné: {self.sauvegarde['level']}")
                print ("fichier sauvegarde chargé")
        except FileNotFoundError:
            print ("sauvegarde.json innexistant")
            self.update_reset_sauvegarde("Sauvegarde non trouvée")  #Page de reset de sauvegarde
        except:
            print("Erreur avec le fichier sauvegarde.json")
            self.update_reset_sauvegarde("Impossible de charger la sauvegarde")
        #+ check integrité controles et level, pour reset independament les controles ou le level

        if self.sauvegarde:
            level = self.sauvegarde["level"]
            if level in data_map:
                try:
                    self.room_name = level   #str du nom de la map, utilisée plus tard pour l'affichage au chargement de salle
                    self.background = data_map[self.room_name][0]    #recupere le background selon la map demandée
                    self.pos_background = get_lefttop(self.background, window, 0)   #place le background au centre de l'ecran, via la fonction de calcul du point
                    self.above_sprite_list = data_map[level][2] #charge la liste des aboves-sprites (images affichées par dessus le joueur)
                    self.above_sprite = None    #l'above-sprite actuellement chargé
                    self.hitbox = data_map[level][1]    #charge l'image des hitbox associée à la map
                    print('salle chargée correctement')
                except:
                    print ("Erreur lors du chargement de la salle")
                    status.on_game = 0
            else:
                print("impossible de trouver le background")
                status.on_game = 0
            self.controls = self.sauvegarde['controls']
            self.player = Player(self.controls, data_map[self.room_name][4], self.pos_background)    #charge le Player


    def update_reset_sauvegarde(self, text):  #fenetre en cas de sauvegarde non chargée
        color_oui = color_non = (67,67,67)  #couleur des boutons
        self.text_reset_save_exc = font.render(text, True,(255,255,255))
        self.text_reset_save = font.render("Voulez-vous en créer une nouvelle ?", True,(255,255,255))
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
                    self.sauvegarde = ''    #Null
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
        self.sauvegarde = {
            "controls": {
                "key_up": 122,
                "key_down": 115,
                "key_left": 113,
                "key_right": 100,
                "key_sprint": 304,
                "key_debug": 119
            },
            "level": "chambre_celeste"
        }
        try:
            with open("data/sauvegarde.json","w") as data:
                json.dump(self.sauvegarde, data, indent=4)
                # data.write(str(self.sauvegarde))
                print("fichier de sauvegarde créé")
                
        except:
            # status.on_game = 0
            print ("/!\ impossible de créer le fichier de sauvegarde")
        
    def hit(self, rect, sens):
        hit = [pygame.Color(0,0,0,0),pygame.Color(0,0,0,0)]
        x = int(rect[0] - self.pos_background[0])
        xx = int(x + rect[2])
        y = int(rect[1] - self.pos_background[1])
        yy = int(y + rect[3])
        if sens == "up":
            hit[0] += self.hitbox.get_at((int(x),int(y)))  #point haut-gauche
            hit[1] += self.hitbox.get_at((int(xx),int(y))) #point haut-droite
        elif sens == "down":
            hit[0] += self.hitbox.get_at((int(x),int(yy))) #point bas-gauche
            hit[1] += self.hitbox.get_at((int(xx),int(yy))) #point bas-droite
        elif sens == "left":
            hit[0] += self.hitbox.get_at((int(x),int(y)))  #point gauche-haut
            hit[1] += self.hitbox.get_at((int(x),int(yy))) #ect...
        elif sens == "right":
            hit[0] += self.hitbox.get_at((int(xx),int(y)))
            hit[1] += self.hitbox.get_at((int(xx),int(yy)))
            #du 1er au 3e NON INCLUS 
        if hit[0][0:3] == (255, 255, 255) and hit[1][0:3] == (255, 255, 255):    #couleur blanche, aucun above
            self.above_sprite = None
            return "can_move"
        elif hit[0][0:3] == (255,0,0) and hit[1][0:3] == (255,0,0):      #couleur rouge, above 1
            self.above_sprite = self.above_sprite_list[0]
            return "can_move"
        elif hit[0][0:3] == (255,106,0) and hit[1][0:3] == (255,106,0):    #couleur orange, above 2
            self.above_sprite = self.above_sprite_list[1]
            return "can_move"
        elif hit[0][0:3] == (255,216,0) and hit[1][0:3] == (255,216,0):         #couleur jaune, above 3
            self.above_sprite = self.above_sprite_list[2]
        #Portes
        if hit[0][0:3] == (255,0,110) or hit[1][0:3] == (255,0,110):      #rose/violet, porte 1
            self.change_room(self.room_name, 1)
        elif hit[0][0:3] == (229,0,99) or hit[1][0:3] == (229,0,99):  # , porte 2
            print("Porte 2")

    def change_room(self, room, porte):
        if porte == 1:
            if room == "chambre_celeste":
                self.room_name = "sdb_chambre_celeste"
                self.above_sprite = None
                pos = (540,460) #position porte 1 chambre
                # self.rect[0], self.rect[1] = 580,460
            elif room == "sdb_chambre_celeste":
                self.room_name = "chambre_celeste"
                self.above_sprite = None
                pos = (920,455) #position porte entrée sdb

        elif room == 2:
            pass    #porte 2
        # pos = data_map[self.room_name][4]

        diff_pos_pieds = self.player.rect_pieds[0] - self.player.rect[0], self.player.rect_pieds[1] - self.player.rect[1]
        diff_pos_img = self.player.rect[0] - self.player.pos_img[0], self.player.rect[1] - self.player.pos_img[1]
        self.player.rect[0],self.player.rect[1] = (pos+self.pos_background)[0],(pos+self.pos_background)[1]
        self.player.rect_pieds[0], self.player.rect_pieds[1] = self.player.rect[0]+diff_pos_pieds[0], self.player.rect[1]+diff_pos_pieds[1]
        self.player.pos_img = self.player.rect[0]-diff_pos_img[0], self.player.rect[1]-diff_pos_img[1]
        self.background = data_map[self.room_name][0]
        self.pos_background = get_lefttop(self.background, self.window, 0)
        self.above_sprite_list = data_map[self.room_name][2]
        self.hitbox = data_map[self.room_name][1]

    def moveRight(self):
        newrect = self.player.rect.move(self.player.vitesse,0)    #prochain rect
        newrect_pieds = self.player.rect_pieds.move(self.player.vitesse,0)
        if self.hit(newrect_pieds,"right") == "can_move":
            self.player.rect = newrect
            self.player.rect_pieds = self.player.rect_pieds.move(self.player.vitesse,0)
            self.player.rect[2] = 20
            self.player.pos_img = (self.player.rect[0]-40,self.player.rect[1]-22)
            # self.rect = self.rect.move(self.vitesse,0)#.clamp(self.rect_background) #eventuellement sur l'image hitbox ?
            self.player.numeroSequence = 3
            self.player.move_sprite = (self.player.vitesse,0)
            if self.player.sens in ["up", "down"]:
                self.player.rect[0] += 11
                # self.rect_pieds[0] += 6
                # self.rect_pieds[2] -= 12
            self.player.sens = "right"
        else:
            pass
        
    def moveLeft(self):
        newrect = self.player.rect.move(-self.player.vitesse,0)
        newrect_pieds = self.player.rect_pieds.move(-self.player.vitesse,0)
        if self.hit(newrect_pieds,"left") == "can_move":
            self.player.rect = newrect
            self.player.rect_pieds = newrect_pieds
            self.player.rect[2] = 20
            self.player.pos_img = (self.player.rect[0]-40,self.player.rect[1]-22)
            # self.rect = self.rect.move(-self.vitesse,0)#.clamp(self.rect_background)
            self.player.numeroSequence = 2
            self.player.move_sprite = (-self.player.vitesse,0)
            if self.player.sens in ["up", "down"]:
                self.player.rect[0] += 11
                # self.rect_pieds[0] += 6
                # self.rect_pieds[2] -= 12
            self.player.sens = "left"
        else:
            pass
    
    def moveUp(self):
        newrect = self.player.rect.move(0,-self.player.vitesse)
        newrect_pieds = self.player.rect_pieds.move(0,-self.player.vitesse)
        if self.hit(newrect_pieds,"up") == "can_move":
            self.player.rect = newrect
            self.player.rect_pieds = newrect_pieds
            self.player.rect[2] = 42
            self.player.pos_img = (self.player.rect[0]-37,self.player.rect[1]-22)
            # self.rect = self.rect.move(0,-self.vitesse)#.clamp(self.rect_background)
            self.player.numeroSequence = 1
            self.player.move_sprite = (0,-self.player.vitesse)
            if self.player.sens in ["left", "right"]:
                self.player.rect[0] -= 11
                # self.rect_pieds[0] -= 6
                # self.rect_pieds[2] += 12
            self.player.sens = "up"
        else:
            pass

    def moveDown(self):
        newrect = self.player.rect.move(0,self.player.vitesse)
        newrect_pieds = self.player.rect_pieds.move(0,self.player.vitesse)
        if self.hit(newrect_pieds,"down") == "can_move":
            self.player.rect = newrect
            self.player.rect_pieds = newrect_pieds
            self.player.rect[2] = 42
            self.player.pos_img = (self.player.rect[0]-37,self.player.rect[1]-22)
            # self.rect = self.rect.move(0,self.vitesse)#.clamp(self.rect_background)
            self.player.numeroSequence = 0
            self.player.move_sprite = (0,self.player.vitesse)
            if self.player.sens in ["left", "right"]:
                self.player.rect[0] -= 11
                # self.rect_pieds[0] -= 6
                # self.rect_pieds[2] += 12
            self.player.sens = "down"
        else:
            pass



