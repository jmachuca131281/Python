from os import system
saldoInicio = 1000000
opcion = int(input(print("Selecciones una opción:\n 1. Ingresar\n 2. Retirar\n 3. Mostrar saldo\n 4. salir")))

def ingresar(monto):
    resultado = saldoInicio + monto
    print(f"Usted ingreso el siguiente monto {monto} y el saldo es {resultado}")

def retirar(monto):
    resultado = saldoInicio - monto
    print(f"Usted retiro el {monto} y el saldo es {resultado}")

def mostrarSaldo(monto):
    resultado = saldoInicio
    print(f"El saldo es {resultado}")

def clear():
    system('cls')

if opcion == 1:
    monto = int(input(print("Ingrese el monto")))
    ingresar(monto)

if opcion == 2:
    monto = int(input(print("Ingrese el monto")))
    retirar(monto)

if opcion == 3:
    monto = int(input(print("Ingrese el monto")))
    mostrarSaldo(monto)

if opcion == 4:
    clear()

