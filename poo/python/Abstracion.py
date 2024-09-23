class Auto():
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo")

mi_auto = Auto()
#Se oculta toda la logica interna que no es necesario
mi_auto.conducir()