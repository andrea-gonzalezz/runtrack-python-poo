from math import *

class Cercle:

    def __init__(self,rayon):
        self.rayon = rayon


    def circonference(self):
        self.circonference = self.rayon * 3.14 *2
        return self.circonference
    
    def aire(self):
        self.aire = pi * (self.rayon **2)
        return self.aire
    
    def diametre(self):
        self.diametre = self.rayon * 2
        return self.diametre

    def afficherInfos(self):
        print(" ")
        print("rayon ", self.rayon)
        print("périmetre ", self.circonference())
        print("aire " , self.aire())
        print("diametre " , self.diametre())

cercle1 = Cercle(4)
cercle2 = Cercle(7)
cercle1.changerRayon()
cercle2.changerRayon()
cercle1.afficherInfos()
cercle2.afficherInfos()




