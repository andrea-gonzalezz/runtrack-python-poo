class Tache:
    def __init__(self, titre, description)
        self.titre = titre
        self.description = description
        self.statut = True


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    
    def ajouterTache(self, tache):
        self.taches.append(tache)
    
    def supprimerTache(self, tache):
        self.taches.remove(tache)
    
    def afficherList(self):
        print(self.taches)

tache1 = Tache("Tache1", "faire la vaisselle", True)

