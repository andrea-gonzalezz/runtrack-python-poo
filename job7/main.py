class Personnage:

    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y += 1

    def haut(self):
        self.y -= 1

personne1 = Personnage(0 , 0)
personne1.haut()
personne1.droite()
personne1.position()