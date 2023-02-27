class Animal:
    
    def __init__(self): 
        self.age = 0
        self.prenom = ''
    
    def vieillir(self):
        print(f"L'animal a {self.age + 1} ans")

    def nommer(self, prenom):
        self.prenom = "Luna"
        print(f"L'animal se nomme {self.prenom}")
        

animal = Animal()
animal.vieillir()
animal.nommer("Luna")

    