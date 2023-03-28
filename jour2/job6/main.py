
class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque =" , self.marque)
        print(f"Année =" , self.annee)
        print(f"Prix =" , self.prix)


    def demarrer(self):
        print("Attention je roule")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, portes):
        self.portes = portes
        Vehicule.__init__(self, marque, annee, prix)
        

    def informationsVehicule(self):
        print(f"Marque =" , self.marque)
        print(f"Année =" , self.annee)
        print(f"Prix =" , self.prix)
        print(f"Portes =" , self.portes)

    def demarrer(self):
        print("Attention je démarre poussez vous")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix, roues):
        self.roues = roues
        Vehicule.__init__(self, marque, annee, prix)

    def informationsVehicule(self):
        print(f"Marque =" , self.marque)
        print(f"Année =" , self.annee)
        print(f"Prix =" , self.prix)
        print(f"Roues =" , self.roues)
    
    def demarrer(self):
        print("Asalto a deux sur la moto on roule !")


vehicule = Vehicule("Toyota", 2010, 10000)
vehicule.informationsVehicule()

voiture = Voiture("Toyota", 2010, 10000, 4)
voiture.informationsVehicule()

moto = Moto("Toyota", 2010, 10000, 2)
moto.informationsVehicule()

vehicule.demarrer()
voiture.demarrer()
moto.demarrer()


