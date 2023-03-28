
class Personne:
    def __init__(self):
        self.age = int(14)

    def afficherAge(self):
        print(f"Vous avez {self.age} ans.")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = int(nouvel_age)


class Eleve(Personne):
    
    def __init__(self):
        Personne.__init__(self)
    
    def allerEnCours(self):
        print("Je vais en cours")
    
    def AffichageAge(self):
        print(f"j'ai {self.age} ans")


class Professeur(Personne):

    def __init__(self, matiereEnseigne, age):
        self.__matiereEnseignee = matiereEnseigne
        self.age = age
        Personne.__init__(self)

    def enseigner(self):
        print("Le cours va commencer")

    def afficherAge(self):
        print(f"j'ai {self.age} ans.")


personne = Personne()
eleve = Eleve()
eleve.bonjour()
eleve.modifierAge(15)
eleve.AffichageAge()
eleve.allerEnCours()




professeur = Professeur("Maths", 40)
professeur.bonjour()
professeur.modifierAge(40)
professeur.afficherAge()
professeur.enseigner()