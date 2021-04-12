# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 21:13:49 2021

@author: manager
"""

class Utilisateur:
    anciennete = 0

    def __init__(self, nom, prenom, age):
        self.name = nom
        self.surname = prenom
        self.old = age

    def getNom(self):
        print ("Je suis ", self.name, " ", self.surname, ".")
        print("J'ai ", self.old, " ans")

class Client(Utilisateur):
    is_client = True

    def __init__(self, nom, prenom, age, email):
        Utilisateur.__init__(self, nom, prenom, age)
        self.mail = email

    def getNom(self):
        Utilisateur.getNom(self)
        print("Adresse mail : ", self.mail, ".")


bello = Client("Bouba", "Bello", 30, "boobabello@gmail.com")
aurelien = Utilisateur("Atangana", "Aurelien", 31)

print("Bonjour tout le monde.\n")
bello.getNom()
print("\n")
aurelien.getNom()

input ("\nAppuyez sur Entrée pour continuer ...")