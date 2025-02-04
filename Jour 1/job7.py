class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

joueur = Personnage(2, 3)  
print(f"Position initiale : {joueur.position()}") 

joueur.gauche()
print(f"Position après déplacement à gauche : {joueur.position()}")  

joueur.droite()
joueur.droite()
print(f"Position après déplacement à droite : {joueur.position()}")  

joueur.haut()
print(f"Position après déplacement en haut : {joueur.position()}")  

joueur.bas()
joueur.bas()
print(f"Position après déplacement en bas : {joueur.position()}")  
