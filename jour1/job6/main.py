
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    
    def setLongueur(self, longueur):
        self.longueur = longueur

    def setLargeur(self, largeur):
        self.largeur = largeur

    def getLongueur(self):
        print(f"La longueur du rectangle est {self.longueur}")
        return self.longueur
    
    def getLargeur(self):
        print(f"La largeur du rectangle est {self.largeur}")
        return self.largeur
    

rectangle = Rectangle(10, 5)
rectangle.getLongueur()
rectangle.getLargeur()
rectangle.setLargeur(10)
rectangle.setLongueur(20)   
rectangle.getLongueur()
rectangle.getLargeur()