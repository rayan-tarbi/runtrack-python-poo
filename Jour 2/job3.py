class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages if isinstance(nombre_de_pages, int) and nombre_de_pages > 0 else 0
        self.__disponible = True  

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def get_disponible(self):
        return self.__disponible

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():  
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.verification(): 
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu.")
        else:
            print(f"Le livre '{self.__titre}' n'a pas été emprunté, il ne peut pas être rendu.")

    def afficher(self):
        statut = "Disponible" if self.__disponible else "Emprunté"
        print(f"Titre: {self.__titre}, Auteur: {self.__auteur}, Nombre de pages: {self.__nombre_de_pages}, Statut: {statut}")

livre = Livre("La livre de la jungle", "Rayan Tarbi", 96)
livre.afficher()

livre.emprunter()  
livre.afficher()

livre.rendre()  
livre.afficher()

livre.rendre()  
