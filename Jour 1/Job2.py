class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation = Operation(12, 3)

print(f"Le nombre1 est {operation.nombre1}")
print(f"Le nombre2 est {operation.nombre2}")
