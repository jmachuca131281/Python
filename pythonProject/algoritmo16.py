opcion = 0

def suma():
    valorUno = int(input(print("Ingrese número uno")))
    valorDos = int(input(print("Ingrese número dos")))
    resultado = valorUno + valorDos
    print(f"La suma es: {resultado}\n")
def resta():
    valorUno = int(input(print("Ingrese número uno")))
    valorDos = int(input(print("Ingrese número dos")))
    resultado = valorUno - valorDos
    print(f"La resta es: {resultado}")
def multiplicacion():
    valorUno = int(input(print("Ingrese número uno")))
    valorDos = int(input(print("Ingrese número dos")))
    resultado = valorUno * valorDos
    print(f"La multiplicación es: {resultado}\n")
def  division():
    valorUno = int(input(print("Ingrese número uno")))
    valorDos = int(input(print("Ingrese número dos")))
    resultado = valorUno / valorDos
    print(f"La diviciión es: {resultado}\n")
def porcentaje():
    valorUno = int(input(print("Ingrese número uno")))
    valorDos = int(input(print("Ingrese número dos")))
    resultado = valorUno % valorDos
    print(f"El procentaje es: {resultado}\n")
def potencia():
    valorUno = int(input(print("Ingrese número de la base:")))
    valorDos = int(input(print("Ingrese número del exponente:")))
    resultado = valorUno ** valorDos
    print(f"La potencia es: {resultado}\n")

while opcion <= 6:
    opcion = int(input(print("Por favor, ingrese una opción\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Divivir\n5. Porcentaje\n6. Potenciar")))
    if opcion == 1:
        suma()
    if opcion == 2:
        resta()
    if opcion == 3:
        multiplicacion()
    if opcion == 4:
        division()
    if opcion == 5:
        porcentaje()
    if opcion == 6:
        potencia()