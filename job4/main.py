class Personne:
    
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(f'je suis {self.prenom} {self.nom}')

personne = Personne("Andrea", "Gonzalez") 
personne.SePresenter()
        