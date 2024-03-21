#Jonathan Arevalo Jonathan Lancheros
class Persona:
    
    def __init__(self,nombre, edad):
        self.__nombre=nombre
        self.__edad=edad

    def getsaludo(self):
        return f"hola el nombre es {self.__nombre} tengo {self.__edad} años"


class estudiante (Persona):
    def __init__(self,nombre,edad,carrera):
        super().__init__(nombre,edad)
        self.__carrera=carrera

    def getsaludo(self):
        return f"{super().getsaludo()} soy de {self.__carrera}"

class Cargo (estudiante):
    def __init__(self,nombre,edad,carrera,cargo):
        super().__init__(nombre,edad,carrera)
        self.__cargo=cargo

    def getsaludo(self):
        return f"{super().getsaludo()} y soy {self.__cargo} "        
contador=0
num=1
while num!=0:
    print("ingresa el nombre")
    nombre=input()
    print("ingrese la edad ")
    edad=input()
    print("ingrese la carrera ")
    carrera=input()
    print("ingrese el cargo")
    cargo=input()
    cargocontador=Cargo(nombre,edad,carrera,cargo)        
    print(cargocontador.getsaludo())
    contador=contador+1
    print("la cantidad de personas ingresados es:",contador)
    print("si desea continuar escoja 1 si no escoja 0")
    num=int(input())
    if num==0:
        break




    
    



