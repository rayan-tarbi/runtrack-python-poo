class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut
    
    def marquerCommeFinie(self):
        self.__statut = "terminée"
    
    def get_statut(self):
        return self.__statut
    
    def get_titre(self):
        return self.__titre
    
    def __str__(self):
        return f"{self.__titre} - {self.__description} [{self.__statut}]"

class ListeDeTaches:
    def __init__(self):
        self.__taches = []
    
    def ajouterTache(self, tache):
        self.__taches.append(tache)
    
    def supprimerTache(self, titre):
        self.__taches = [t for t in self.__taches if t.get_titre() != titre]
    
    def afficherListe(self):
        for tache in self.__taches:
            print(tache)
    
    def filterListe(self, statut):
        return [t for t in self.__taches if t.get_statut() == statut]

tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Réviser Python", "Pratiquer les classes et objets")
tache3 = Tache("Faire du sport", "Aller courir 30 minutes")

liste = ListeDeTaches()
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

print("Liste des tâches :")
liste.afficherListe()

tache1.marquerCommeFinie()

print("\nTâches après mise à jour :")
liste.afficherListe()

print("\nTâches à faire :")
for tache in liste.filterListe("à faire"):
    print(tache)
