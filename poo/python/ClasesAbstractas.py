#Es una clase que no podemos instanciar
#Obliga a las subclases a usar los metodos del padre, es como un contrato
from abc import ABC,abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def trabajar(self):
        pass

    def presentarse(self):
        print(f'Hola me llamo: {self.nombre} y tengo {self.edad} años')


class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def trabajar():
        pass


estudiante = Estudiante("Duberly",20,"Masculino","Programador")

estudiante.presentarse()
