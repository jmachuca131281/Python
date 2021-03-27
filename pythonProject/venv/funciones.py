def saludar():
    print("Esta es una función")

saludar()

def saludar(nombre):
    print(f"El nombre es {nombre}")

nombre = "Charly"
saludar(nombre)

def saludar(nombre, apellido):
    print(f"El nombre es {nombre} y el apellido es {apellido}")

nombre = "Miguis"
apellido = "Duarte"

nombreApellido = nombre + apellido
saludar(nombre, apellido)

def saludar(edad, sexo):
    print(f"La esdad es {edad} y el sex es {sexo}")

edad = 123
sexo = "muy poco"
saludar(edad, sexo)

def suma(uno, dos):
    suma = uno + dos
    return suma
resultado = suma(321, 3)
print(resultado)
