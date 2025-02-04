class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def se_presenter(self):
        return f"Je suis {self.prenom} {self.nom}"

personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupond")

print(personne1.se_presenter())
print(personne2.se_presenter())
