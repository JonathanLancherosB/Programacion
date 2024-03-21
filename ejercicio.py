class Persona:
    def __init__(self, nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    def getSaludo(self):
        return f"mi nombre es {self.__nombre} tengo {self.__edad} años"
    
class Estudiante (Persona):
    def __init__(self, nombre,edad,carrera):
        super().__init__(nombre, edad)
        self.__carrera = carrera 

    def getSaludo(self):
        return f"{super().getSaludo()} y estudio {self.__carrera}"

        

Estudiante = Estudiante("Jonathan Lancheros", 19, "Ingenieria de sistemas y computacion")
print(Estudiante.getSaludo())