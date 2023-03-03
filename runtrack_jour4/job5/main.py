class Forme:

    def __init__(self):
        pass

    def aire(self):
        return 0
    
class Rectangle(Forme):

    def __init__(self,hauteur, largeur):
        Forme.__init__(self)
        self.hauteur = hauteur
        self.largeur = largeur

    def aire(self):
        return self.hauteur * self.largeur
    
    
class Cercle(Forme):

    def __init__(self, radius):
        Forme.__init__(self)
        self.radius = radius

    def aire(self):
        return (self.radius * self.radius) * 3.14
    

cercle = Cercle(10)

print(cercle.aire())

