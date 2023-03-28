
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

    def getLongueur(self):
        print(f"Le rectangle a une longueur de : {self.longueur}")

    def getLargeur(self):
        print(f"Le rectangle a une largeur de {self.largeur}")

    def perimetre(self):
        return (self.__longueur + self.__largeur) *2
    
    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur
        

    def setHauteur(self, hauteur):
        self.__hauteur = hauteur

    def getHauteur(self):
        print(f"Le parallelepipede a une hauteur de {self.__hauteur}")


    def volume(self):
        return self.surface() * self.__hauteur


rectangle = Rectangle(10, 5)
print(rectangle.surface())
print(rectangle.perimetre())

parallelepipede = Parallelepipede(10,5, 2)
print(parallelepipede.volume())

rectangle.setLongueur(20)
rectangle.getLongueur()
