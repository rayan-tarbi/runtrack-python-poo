class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages if isinstance(nombre_de_pages, int) and nombre_de_pages > 0 else 0

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def afficher(self):
        print(f"Titre: {self.__titre}, Auteur: {self.__auteur}, Nombre de pages: {self.__nombre_de_pages}")

livre = Livre("Le livre de la jungle by flappou", "Tarbi Rayan", 12)
livre.afficher()

livre.set_nombre_de_pages(120)  
livre.afficher()

livre.set_nombre_de_pages(-10)  
livre.afficher()
