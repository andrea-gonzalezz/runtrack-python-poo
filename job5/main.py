class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f'{self.x} {self.y}')

    def afficherX(self):
        print(f'{self.x}')

    def afficherY(self):
        print(f'{self.y}')

    def changerX(self, x):
        self.x = x
        print(f'{self.x}')

    def changerY(self, y):
        self.y = y
        print(f'{self.y}')


punto = Point(10, 5)
punto.afficherLesPoints()

punto.afficherX()
punto.afficherY()

punto.changerX(50)
punto.changerY(48)

