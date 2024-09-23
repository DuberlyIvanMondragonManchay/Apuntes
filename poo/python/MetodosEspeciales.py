class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'{self.nombre}, {self.edad}'
    
    def __repr__(self):
        return f'{self.nombre}, {self.edad}'
    
    def __add__(self,otro):
        nuevo_valor = otro
        return Persona(self.nombre+otro.nombre,nuevo_valor) 

dalto = Persona("Lucas",21)

print(dalto)

lista = (1,2,3,4)
print(lista)
        
