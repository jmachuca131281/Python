opcion = int(input(print(
    "Por favor, ingrese una opción\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Divivir\n5. Porcentaje\n6. Potenciar")))
if opcion == 1:
    valorUno = int(input(print("Ingrese el primer número")))
    valorDos = int(input(print("Ingrese el segundo número")))
    resultado = valorUno + valorDos
    print(f"El resultado de la suma es: {resultado}")
if opcion == 2:
    valorUno = int(input(print("Ingrese el primer número")))
    valorDos = int(input(print("Ingrese el segundo número")))
    resultado = valorUno - valorDos
    print(f"El resultado de la resta es: {resultado}")
if opcion == 3:
    valorUno = int(input(print("Ingrese el primer número")))
    valorDos = int(input(print("Ingrese el segundo número")))
    resultado = valorUno * valorDos
    print(f"El resultado de la multiplicación es: {resultado}")
if opcion == 4:
    valorUno = int(input(print("Ingrese el primer número")))
    valorDos = int(input(print("Ingrese el segundo número")))
    resultado = valorUno / valorDos
    print(f"El resultado de la división es: {resultado}")
if opcion == 5:
    valorUno = int(input(print("Ingrese el primer número")))
    valorDos = int(input(print("Ingrese el segundo número")))
    resultado = valorUno % valorDos
    print(f"El resultado del porcentaje es: {resultado}")
if opcion == 6:
    valorUno = int(input(print("Ingrese la base")))
    valorDos = int(input(print("Ingrese el exponente")))
    resultado = valorUno ** valorDos
    print(f"La potencia es: {resultado}")
