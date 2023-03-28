class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius
        Forme.__init__(self)

    
    def aire(self):
        return self.__radius * self.__radius * 3.14
    

cercle = Cercle(10)
print(cercle.aire())
    

