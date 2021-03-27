numero = int(input(print("Ingrese el número de elementos")))

arrayEdad = []
for x in range(0, numero):
     arrayEdad.append(int(input(print(f"Sr. usuario digite la edad de la {x}: "))))

for x in range(0, numero):
     print(f"La edad en la posición {x} es {arrayEdad[x]}")