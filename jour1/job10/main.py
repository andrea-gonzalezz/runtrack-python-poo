class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, enmarche, reservoir):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__enmarche = False
        self.__reservoir = 50
        
    def setMarque(self, marque):
        self.__marque = marque

    def setModele(self, modele):
        self.__modele = modele

    def setAnnee(self, annee):
        self.__annee = annee

    def setKilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def getMarque(self):
        print(f"Marque = {self.__marque}")
        return self.__marque    
    
    def getModele(self):
        print(f"Modele = {self.__modele}")
        return self.__modele
    
    def getAnnee(self):
        print(f"Annee = {self.__annee}")
        return self.__annee
    
    def getKilometrage(self):
        print(f"Kilometrage = {self.__kilometrage}")
        return self.__kilometrage
    
    def setResevoire(self, reservoir):
        self.__reservoir = reservoir

    def getResevoire(self):
        print(f"Resevoire = {self.__reservoir}")
        return self.__reservoir
    
    def demarrer(self):
        if self.__verifier_plein():
            if self.__reservoir > 5:
                self.__enmarche = True
            print(f"La voiture {self.__marque} {self.__modele} est demarree")
        print(f"La voiture {self.__marque} {self.__modele} est demarree")

    def arreter(self):
        self.__en_marche = False
        print(f"La voiture {self.__marque} {self.__modele} est arretee")

    def __verifier_plein(self):
        return self.__reservoir == 50


voiture = Voiture("Renault", "Clio", 2010, 100000, False, 50)
voiture.getMarque()
voiture.getModele()
voiture.getAnnee()
voiture.getKilometrage()
voiture.demarrer()  
voiture.arreter()
voiture.setResevoire(1)
       

    