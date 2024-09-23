#Qué es un decorador
#Toma una funcion como entrada y lo modifica

def decorador(function):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        function()
        print("Despues de llamar a la funcion")
    return funcion_modificada


# def saludo():
#     print("HOla saludando")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola Dalto como andas")

saludo()
