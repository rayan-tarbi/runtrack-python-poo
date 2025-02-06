class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False  
        self.__reservoir = 50 

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_reservoir(self, quantite):
        if quantite >= 0:
            self.__reservoir = quantite
        else:
            print("Erreur : La quantité de carburant ne peut pas être négative.")

    def __verifier_plein(self):
        return self.__reservoir  

    def demarrer(self):
        if self.__verifier_plein() > 5:  
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Impossible de démarrer, le réservoir est trop bas !")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")

    def afficher_info(self):
        etat = "En marche" if self.__en_marche else "À l'arrêt"
        print(f"Marque: {self.__marque}, Modèle: {self.__modele}, Année: {self.__annee}")
        print(f"Kilométrage: {self.__kilometrage} km, Réservoir: {self.__reservoir} L, État: {etat}")

voiture1 = Voiture("Toyota", "Corolla", 2020, 30000)

voiture1.afficher_info()

voiture1.demarrer()
voiture1.afficher_info()

voiture1.arreter()
voiture1.afficher_info()

voiture1.set_reservoir(3)
voiture1.demarrer()
