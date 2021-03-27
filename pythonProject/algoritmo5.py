saldo = 1000000

opcion = int(input(print("Ingrese la operacón a realizar:"
          "\n1. Ingrasar dirnero"
          "\n2. Retirar dinero"
          "\n3. Mostrar Dinero"
          "\n4. Salida"
          )))
if opcion == 1:
    monto = int(input(print("Ingrese el monto: ")))
    resultado = saldo + monto
    print(f"El resultado es: {resultado}")
elif opcion == 2:
    monto = int(input(print("Ingrese el monto: ")))
    resultado = saldo - monto
    print(f"El resultado es: {resultado}")
elif opcion == 3:
    print(f"El resultado es: {saldo}")
elif opcion == 4:
    print("Gracias vielva pronto")