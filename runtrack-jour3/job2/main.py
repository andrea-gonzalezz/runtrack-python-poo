class CompteBancaire:
    def __init__(self, compte, nom, prenom, solde):
        self.__compte = compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = True

    def afficher(self):
        print("Numéro de compte :", self.__compte)
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("Solde :", self.__solde)
        print("Decouvert:", self.__decouvert)
    
    def afficherSolde(self):
        print("Solde :", self.__solde)
    
    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de, ", montant)

    def retrait(self, retrait):
        self.__solde -= retrait 
        print(f"Retrait de" ,retrait, "effectué.")
        print("Nouveau solde:", self.__solde)
        if retrait >= self.__solde or self.__solde < 0:
            self.__decouvert = False
            print("Fonds indisponibles, veuillez choisir un montant plus petit")
        else:
            self.__decouvert = True
    
    def agios(self):
        if self.__solde < 0:
            self.__solde - 8
            print("Intervention bancaire. Nouveau solde:", self.__solde - 8)
    
    def virement(self, beneficiaire, montant):
        beneficiaire.__solde += montant
        self.__solde  -= montant
        print("Le virement a été effectué")
    


comptebancaire = CompteBancaire("Premier client du monde","Gonzalez","Andrea",1500)


comptebancaire.afficher()
comptebancaire.versement(500)
comptebancaire.retrait(2500)
comptebancaire.agios()

nico = CompteBancaire("Pire client", "Nico", "Rigal", 1)
nico.virement("Nico ", 50)




       