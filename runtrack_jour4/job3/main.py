class Rectangle:

    def __init__(self,longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2*(self.__longueur + self.__largeur)
    
    def surface(self):
        return (self.__longueur * self.__largeur)
    
    def getlongueur(self):
        return self.__longueur
    
    def getlargeur(self):
        return self.__largeur
    
    def setlongueur(self, longueur):
        self.__longueur = longueur

    def setlargeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):

    def __init__(self,longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        return self.surface() * self.hauteur
    

rectangle = Rectangle(10,5)
parallelepipede = Parallelepipede(10,5,100)

print(rectangle.perimetre())
print(rectangle.surface())
print(parallelepipede.volume())

