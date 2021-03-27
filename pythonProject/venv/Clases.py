class ClaseSilla:
    color = "blanco"
    precio = 100

objetosSilla = ClaseSilla()
objetosSilla.color
print(objetosSilla.color)
objetosSilla.precio
print(objetosSilla.precio)

objSilla2 = ClaseSilla()
objSilla2.color = "Silla ortopedica"
objSilla2.precio = 199
print(f"El nuevo color es {objSilla2.color} y el precio es {objSilla2.precio}")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print("Hola, me llamo {} y tengo {} años".format(self.nombre, self.edad))

clasePersona = Persona("Josman", 39)
print(clasePersona.nombre)
print(clasePersona.edad)

clasePersona.saludar()