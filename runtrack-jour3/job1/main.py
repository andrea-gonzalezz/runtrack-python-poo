class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population
    
    def getnom(self):
        return self.__nom
    
    def setnom(self,nom):
        self.__nom = nom
        return self.__nom
    
    def getpopulation(self):
        return self.__population
    
    def setpopulation(self,population):
        self.__population = population
        return self.__population
    
    
ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)
print(f"Population de la ville de {ville1.getnom()}: {ville1.getpopulation()}")
print(f"Population de la ville de {ville2.getnom()}: {ville2.getpopulation()}")


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville


    def getnom(self):
        return self.__nom
    
    def setnom(self, nom):
        self.__nom = nom
        return self.__nom
    
    def getage(self):
        return self.__age
    
    def setage(self, age):
        self.__age = age
        return self.__age
    
    def getville(self):
        return self.__ville
    
    def setville(self, ville):
        self.__ville = ville
        return self.__ville

    def ajouterPopulation(self):
        self.__ville.setpopulation(self.__ville.getpopulation() + 1)
        print(f"La population de {self.__ville.getnom()} a été mise a jour: {self.__ville.getpopulation()}")


personne1 = Personne("John", 45, ville1)
personne2 = Personne("Myrtille", 4, ville1)
personne3 = Personne("Chloé", 18, ville2)

personne1.ajouterPopulation()
personne2.ajouterPopulation()
personne3.ajouterPopulation()








    
