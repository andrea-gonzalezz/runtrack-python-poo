
class Livre: 
    def __init__(self, titre, auteur, pages, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True
        
    def setTitre(self, titre):
        self.__titre = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur

    def setPages(self, pages):
        self.__pages = pages

    def getTitre(self):
        print(f"Le titre du livre est {self.__titre}")
        return self.__titre
    
    def getAuteur(self):
        print(f"L'auteur du livre est {self.__auteur}")
        return self.__auteur
    
    def getPages(self):
        print(f"Le nombre de pages du livre est {self.__pages}")
        return self.__pages
    
    def verification(self):
        if self.__disponible == True:
            print("Le livre est disponible")
            return True
        else:
            print("Le livre n'est pas disponible")
            return False
    
    def emprunter(self):
        if self.__disponible == True:
            self.__disponible = False
            print("Le livre a été emprunté")
        else:
            print("Le livre n'est pas disponible")

    def rendre(self):
        if self.verification() == False:
            self.__disponible = True
            print("Le livre a été rendu")
    
livre = Livre(" ", " ", 0, True)
livre.setTitre("20000 lieues sous les mers")
livre.setAuteur("Jules Verne")
livre.setPages(300)
livre.getTitre()
livre.getAuteur()
livre.getPages()

livre.rendre()
livre.emprunter()
livre.emprunter()
