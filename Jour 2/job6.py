class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  
        self.__statut = "En cours"  

    def get_numero_commande(self):
        return self.__numero_commande

    def get_statut(self):
        return self.__statut

    def ajouter_plat(self, nom_plat, prix):
        if prix > 0:
            self.__plats_commandes[nom_plat] = prix
            print(f"Le plat '{nom_plat}' a été ajouté à la commande.")
        else:
            print("Erreur : Le prix du plat doit être positif.")

    def __calculer_total(self):
        return sum(self.__plats_commandes.values())

    def afficher_commande(self):
        print(f"Commande N°{self.__numero_commande} - Statut: {self.__statut}")
        if self.__plats_commandes:
            print("Plats commandés :")
            for plat, prix in self.__plats_commandes.items():
                print(f" - {plat} : {prix} €")
            total = self.__calculer_total()
            print(f"Total à payer : {total:.2f} € (hors TVA)")
        else:
            print("Aucun plat n'a été ajouté à cette commande.")

    def calculer_tva(self):
        total = self.__calculer_total()
        return total * 0.20

    def annuler_commande(self):
        self.__statut = "Annulée"
        self.__plats_commandes.clear()
        print("La commande a été annulée.")

    def terminer_commande(self):
        if self.__plats_commandes:
            self.__statut = "Terminée"
            print("La commande est maintenant terminée.")
        else:
            print("Impossible de terminer une commande vide.")

commande1 = Commande(101)

commande1.ajouter_plat("Pizza Margherita", 12)
commande1.ajouter_plat("Pâtes Carbonara", 15)
commande1.ajouter_plat("Tiramisu", 6)

commande1.afficher_commande()

print(f"TVA à payer : {commande1.calculer_tva():.2f} €")

commande1.terminer_commande()
commande1.afficher_commande()

commande1.annuler_commande()
commande1.afficher_commande()
