class Produit:
    def __init__(self, nom, prixHT, TVA=0.2):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)

    def afficherInfos(self):
        return (f"Produit : {self.nom}, Prix HT : {self.prixHT:.2f}€, "
                f"TVA : {self.TVA*100}%, Prix TTC : {self.calculerPrixTTC():.2f}€")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def getPrixTTC(self):
        return self.calculerPrixTTC()

produit1 = Produit("Ordinateur", 800)
produit2 = Produit("Smartphone", 600)

print(produit1.afficherInfos())
print(produit2.afficherInfos())

produit1.modifierNom("PC Gamer")
produit1.modifierPrixHT(1200)

produit2.modifierNom("iPhone")
produit2.modifierPrixHT(900)

print(produit1.afficherInfos())
print(produit2.afficherInfos())
