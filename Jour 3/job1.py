class City:
    def __init__(self, name, population):
        self.__name = name
        self.__population = population

    def add_inhabitant(self):
        self.__population += 1

    def get_population(self):
        return self.__population

    def get_name(self):
        return self.__name

class Person:
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city
        self.add_to_population()
    
    def add_to_population(self):
        self.__city.add_inhabitant()

paris = City("Paris", 1000000)
marseille = City("Marseille", 861635)

print(f"Population in Paris before: {paris.get_population()}")
print(f"Population in Marseille before: {marseille.get_population()}")

john = Person("John", 45, paris)
myrtille = Person("Myrtille", 4, paris)
chloe = Person("Chloé", 18, marseille)

print(f"Population in Paris after: {paris.get_population()}")
print(f"Population in Marseille after: {marseille.get_population()}")