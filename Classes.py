from Constantes import *
#
# Classes associées au jeu
#
class Parametres(): #En base de donnée soon
    def __init__(self):
        self.Taille_fenetre = (1280,720) #Par defaut, modifié dans les parametres du menu

class controle():
    def __init__(self):
        self.droite = [K_d,K_RIGHT]
        self.gauche = [K_q,K_LEFT]
        self.haut = [K_z,K_UP]
        self.bas = [K_s, K_DOWN]

Parametres = Parametres()
Parametres.controle = controle()

class Player():
    def __init__(self):
        self.sprite = Celeste_bas   #Orientation/sprite par defaut
        self.orientation = "bas"
        self.pos_x = 265    #par rapport au background
        self.pos_y = 155
        self.pos = (265,155)

    def deplacement(self, event_type, event_key, Player):
        global compteur_sprite
        print (compteur_sprite)
        Player.pos_old = Player.pos #Pour les colisions, le retour à l'ancienne pos
        if event_type == KEYDOWN:

            if event_key in Parametres.controle.droite:
                if compteur_sprite >= len(Celeste_Anim_Droite)-1:
                    compteur_sprite = 0
                else:
                    compteur_sprite += 1
                Player.pos = Player.pos.move(5,0)
                Player.sprite = Celeste_Anim_Droite[compteur_sprite]
                Player.sprite_orientation = "droite"
                ####
            elif event_key in Parametres.controle.gauche:
                if compteur_sprite >= len(Celeste_Anim_Gauche)-1:
                    compteur_sprite = 0
                else:
                    compteur_sprite += 1
                Player.pos = Player.pos.move(-5,0)
                Player.sprite = Celeste_Anim_Gauche[compteur_sprite]
                Player.sprite_orientation = "gauche"
                ####
            if event_key in Parametres.controle.haut:
                if compteur_sprite >= len(Celeste_Anim_Haut)-1:
                    compteur_sprite = 0
                else:
                    compteur_sprite += 1
                Player.pos = Player.pos.move(0,-5)
                Player.sprite = Celeste_Anim_Haut[compteur_sprite]
                Player.sprite_orientation = "haut"
                ####
            elif event_key in Parametres.controle.bas:
                if compteur_sprite >= len(Celeste_Anim_Bas)-1:
                    compteur_sprite = 0
                else:
                    compteur_sprite += 1
                Player.pos = Player.pos.move(0,5)
                Player.sprite = Celeste_Anim_Bas[compteur_sprite]
                Player.sprite_orientation = "bas"
        elif event_key == KEYUP:
            compteur_sprite = 0
            Player.sprite = Celeste_dico[Player.sprite_orientation][0]



class background():
    def __init__(self):
        self.img = ChambreCeleste    #ici par defaut, dernier background en Save en base de donnée soon
        # self.x,self.y,self.L,self.w = self.img.get_rect() #Length -> longueur(y) | width -> Largeur(x)
        # self.x = Parametres.w_fenetre/2 - self.w/2
        # self.y = Parametres.L_fenetre/2 - self.L/2
        self.pos = (Parametres.Taille_fenetre[0]/2 - self.img.get_rect()[2]/2, Parametres.Taille_fenetre[1]/2 - self.img.get_rect()[3]/2)
        
