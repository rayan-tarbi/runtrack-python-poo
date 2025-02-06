class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts = 0
        self.__passes_decisives = 0
        self.__cartons_jaunes = 0
        self.__cartons_rouges = 0
    
    def marquerUnBut(self):
        self.__buts += 1
    
    def effectuerUnePasseDecisive(self):
        self.__passes_decisives += 1
    
    def recevoirUnCartonJaune(self):
        self.__cartons_jaunes += 1
    
    def recevoirUnCartonRouge(self):
        self.__cartons_rouges += 1
    
    def afficherStatistiques(self):
        return f"{self.__nom} (#{self.__numero}, {self.__position}) - Buts: {self.__buts}, Passes: {self.__passes_decisives}, Jaunes: {self.__cartons_jaunes}, Rouges: {self.__cartons_rouges}"

class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.__joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self):
        for joueur in self.__joueurs:
            print(joueur.afficherStatistiques())
    
    def mettreAJourStatistiquesJoueur(self, nom, action):
        for joueur in self.__joueurs:
            if joueur._Joueur__nom == nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                break

# Création des joueurs
joueur1 = Joueur("Mbappé", 10, "Attaquant")
joueur2 = Joueur("Kanté", 7, "Milieu")
joueur3 = Joueur("Varane", 4, "Défenseur")

# Création de l'équipe
equipe = Equipe("Les Bleus")
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)

# Simulation d'un match
equipe.mettreAJourStatistiquesJoueur("Mbappé", "but")
equipe.mettreAJourStatistiquesJoueur("Kanté", "passe")
equipe.mettreAJourStatistiquesJoueur("Varane", "jaune")

# Affichage des statistiques des joueurs
equipe.afficherStatistiquesJoueurs()
