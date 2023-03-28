
class Animal:
    def __init__(self, nom, age):
        self.nom = " "
        self.age = 0

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.nom = "Luna"

animal = Animal(" ", 0)
print(f"L'age de l'animal est {animal.age}")
animal.vieillir()
print(f"L'age de l'animal est {animal.age}")
animal.nommer("Luna")
print(f"Le nom de l'animal est {animal.nom}")
  