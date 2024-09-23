class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre

persona = Persona("Duberly",20)
persona.nombre = "Pepe"
nombre = persona.nombre

print(nombre)
