numero = int(input(print("Ingrese el número de elementos")))
arrayEdad = []

for x in range(0, numero):
     arrayEdad.append(int(input(print(f"Sr. usuario digite la edad de {x} posición: "))))

for x in range(0, numero):
     if arrayEdad[x] >= 18:
          print(f"Las siguientes edades son de mayores de edad: {arrayEdad[x]}" )
     if arrayEdad[x] < 18:
          print(f"Las siguientes edades son menores de edad: {arrayEdad[x]}")