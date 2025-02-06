import random

class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie
    
    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.recevoirDegats(degats)
        print(f"{self.__nom} attaque {adversaire.get_nom()} et lui inflige {degats} points de dégâts !")
    
    def recevoirDegats(self, degats):
        self.__vie -= degats
        if self.__vie < 0:
            self.__vie = 0
        print(f"{self.__nom} a maintenant {self.__vie} points de vie.")
    
    def estVivant(self):
        return self.__vie > 0
    
    def get_nom(self):
        return self.__nom
    
    def get_vie(self):
        return self.__vie

class Jeu:
    def __init__(self):
        self.__niveau = None
    
    def choisirNiveau(self):
        self.__niveau = input("Choisissez un niveau (facile, moyen, difficile) : ").lower()
    
    def lancerJeu(self):
        if self.__niveau == "facile":
            vie_joueur = 100
            vie_ennemi = 50
        elif self.__niveau == "moyen":
            vie_joueur = 75
            vie_ennemi = 75
        else:
            vie_joueur = 50
            vie_ennemi = 100
        
        joueur = Personnage("Héros", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)
        
        while joueur.estVivant() and ennemi.estVivant():
            input("Appuyez sur Entrée pour attaquer...")
            joueur.attaquer(ennemi)
            
            if ennemi.estVivant():
                ennemi.attaquer(joueur)
        
        if joueur.estVivant():
            print("Bravo ! Vous avez gagné !")
        else:
            print("Game Over. L'ennemi a gagné.")

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
