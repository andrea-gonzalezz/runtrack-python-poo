class Vehicule:

    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationVehicule(self):
        print(f'Marque = {self.marque}')
        print(f"Modele = {self.modele}")
        print(f'annee = {self.annee}')
        print(f'Prix = {self.prix}')

    def demarrer(self):
        print("Attention je roule!")



class Voiture(Vehicule):

    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.portes = 4

    def informationVehicule(self):
        print(f'Marque = {self.marque}')
        print(f"Modele = {self.modele}")
        print(f'annee = {self.annee}')
        print(f'Prix = {self.prix}')
        print(f'Portes = {self.portes}')

    def demarrer(self):
        print("Je roule en Mercedes je prends le bus de la RTM")


class Moto(Vehicule):

    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roues = 2

    def informationVehicule(self):
        print(f'Marque = {self.marque}')
        print(f"Modele = {self.modele}")
        print(f'annee = {self.annee}')
        print(f'Prix = {self.prix}')
        print(f'Roues = {self.roues}')

    def demarrer(self):
        print("Top chrono a deux sur la moto!")

    


vehicule = Vehicule("renault", "CACA", 1990, 2000)
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)


vehicule.informationVehicule()
voiture.informationVehicule()

moto = Moto("Yamaha", "1200 Max", 1987, 4500)
moto.informationVehicule()

moto.demarrer()
voiture.demarrer()


