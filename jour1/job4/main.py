
class Personne: 
    def __init__(self, nom, prenom): 
        self.nom = nom 
        self.prenom = prenom 
    
    def SePresenter(self): 
        print("Je suis", self.prenom, self.nom)


personne = Personne("Doe", "John")
personne2 = Personne("Gonzalez", "Andrea")
print(personne.SePresenter())
print(personne2.SePresenter())