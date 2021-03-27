numeroLlegada = int(input(print("Ingrese el número de llegada")))

for x in range(numeroLlegada):
    print(x)
    if (x % 2) != 0:
        print("Impar")
    if (x % 2) == 0:
        print("par")