class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0
    

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        Forme.__init__(self)

    def aire(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        return self.__longueur * self.__largeur
    

rectangle = Rectangle(10, 5)
print(rectangle.aire(10, 5))