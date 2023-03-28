
class Student: 

    def __init__(self, nom, prenom, numero, credits):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credits = 0

    def setNom(self, nom):
        self.__nom = nom

    def setPrenom(self, prenom):
        self.__prenom = prenom

    def setNumero(self, numero):
        self.__numero = numero

    def getNom(self):
        print(f"Nom = {self.__nom}")
        return self.__nom
    
    def getPrenom(self):
        print(f"Prenom = {self.__prenom}")
        return self.__prenom
    
    def getNumero(self):
        print(f"Numero = {self.__numero}")
        return self.__numero
    
    def add_credits(self):
        if credits > 0: 
            self.__credits += credits
            print(f"Le nombre de credits de {self.__prenom} {self.__nom} est {self.__credits}")
            self.__level = self.__studenEval()
            return self.__credits

    def __studenEval(self):
        if self.__credits >= 90:
            print("Excellent")
        
        elif self.__credits >= 80:
            print("Très bien")

        elif self.__credits >= 70:
            print("Bien")

        elif self.__credits >= 60:
            print("Passable")

        else:
            print("Insuffisant")

    def StudentInfo(self):
        print (f"Nom = {self.__nom} \
              \nPrenom = {self.__prenom}\
               \nNumero = {self.__numero}\
              \nCredits = {self.__credits}\
               \nNiveau = {self.__level}")

student = Student("Doe", "John", 123456, 80)
student.setNom("Doe")
student.setPrenom("John")
student.setNumero(123456)
Student.add_credits(80)