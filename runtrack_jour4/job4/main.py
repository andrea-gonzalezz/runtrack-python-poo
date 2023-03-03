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
    
rectangle = Rectangle(10,5)

print(rectangle.aire())

