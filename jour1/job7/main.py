
class Livre: 
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        
    def setTitre(self, titre):
        self.__titre = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur

    def setPages(self, pages):
        if self.__pages < 0:
            self.__pages = pages
        else:
            print("Le nombre de pages doit etre superieur a 0")
            
            
    def getTitre(self):
        print(f"Le titre du livre est {self.__titre}")
        return self.__titre
    
    def getAuteur(self):
        print(f"L'auteur du livre est {self.__auteur}")
        return self.__auteur
    
    def getPages(self):
        print(f"Le nombre de pages du livre est {self.__pages}")
        return self.__pages
    
livre = Livre(" ", " ", 0)
livre.setTitre("20000 lieues sous les mers")
livre.setAuteur("Jules Verne")
livre.setPages(-25)
livre.getTitre()
livre.getAuteur()
livre.getPages()
