class Rectangle: 

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def setLongueur(self, longueur):
        self.longueur = longueur

    def setLargeur(self, largeur):
        self.largeur = largeur

    def getLongueur(self):
        print(f"Le rectangle a une longueur de : {self.longueur}")

    def getLargeur(self):
        print(f"Le rectangle a une largeur de {self.largeur}")

rectangle1 = Rectangle(10,5)
rectangle1.getLongueur()
rectangle1.getLargeur()
rectangle1.setLongueur(18)
rectangle1.setLargeur(10)