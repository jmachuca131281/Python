numero = int(input(print("Señor usuario digite el numero de elementos del arreglo: ")))
letra = []
for x in range(0, numero):
    letra.append(str(input(print(f"Sr. usuario digite {x} letra del nombre: "))))
    if letra[x] == "a":
        letra.remove("a")
        letra.append("@")
    if letra[x] == "e":
        letra.remove("e")
        letra.append("3")
    if letra[x] == "o":
        letra.remove("o")
        letra.append("0")

separator = ""
print(separator.join(letra))