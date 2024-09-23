class Persona:
    def __init__(self,edad,nombre,nacionalidad):
        self.edad = edad
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola estoy hablando")

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f'Mi habilidad es {self.habilidad} ')
#Herencia simple
class Empleado(Persona):
    def __init__(self,edad,nombre,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad) #Hereda de la clase padre
        self.trabajo = trabajo
        self.salario = salario
    pass

class EmpleadoArtista(Persona,Artista):
    def __init__(self,edad,nombre,nacionalidad,salario,habilidad,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    

    def mostrar_habilidad(self):
        print("No tengo jaja")
    
    def presentarse(self):
        super().mostrar_habilidad()

#Herencia multiple

empleado = EmpleadoArtista("19","Duberly","Perú",1200,"Cantar","Yape")
print(empleado.nacionalidad)
empleado.hablar()
empleado.presentarse()

herencia = issubclass(EmpleadoArtista,Persona)
