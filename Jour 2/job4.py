class Student:
    def __init__(self, nom, prenom, student_id):
        self.__nom = nom
        self.__prenom = prenom
        self.__student_id = student_id
        self.__credits = 0  
        self.__level = self.__student_eval()  

    def get_credits(self):
        return self.__credits

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()  
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"Id = {self.__student_id}")
        print(f"Niveau = {self.__level}")

etudiant = Student("John", "Doe", 145)

etudiant.add_credits(10)
etudiant.add_credits(10)
etudiant.add_credits(10)

print(f"Le nombre de crédits de John Doe est de {etudiant.get_credits()} points")

etudiant.student_info()
