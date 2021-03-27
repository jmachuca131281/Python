saldoInicial = 1000000
opcion = 0


def ingresarDinero(a):
    saldo = saldoInicial + a
    print(f"Su saldo es {saldo}\n")

def retirarDinero(a):
    saldo = saldoInicial - a
    print(f"Su saldo es {saldo}\n")

while opcion < 4:
    opcion = int(input(print("Ingrese la operacón a realizar:\n1. Ingrasar dirnero\n2. Retirar dinero\n3. Mostrar Dinero \n4. Salida")))
    if opcion == 1:
        dinero = int(input(print("Por favor, igrese monto")))
        ingresarDinero(dinero)
    if opcion == 2:
        dinero = int(input(print("Por favor, igrese monto")))
        retirarDinero(dinero)
    if opcion == 3:
        print(f"El saldo es {saldoInicial}\n")
    if opcion == 4:
        print("Adios mundo cruel")
        break