class Celular:
    #Esta función se ejecuta automáticamente cada ves que  creamos un objeto
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #Los métodos son para definir que acciones puede acer nuestro objeto
    def llamar(self):
        print("Estas haciendo un llamado")

celular1 = Celular("Samsung","A10","48MP")

print(celular1.marca)

celular1.llamar()
