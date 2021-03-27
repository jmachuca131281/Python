llegara = int(input(print("Señor usuario digite el número hasta donde llegara la multiplicación")))
multiplo = int(input(print("Señor usuraio digite el multiplo")))

for valor in range(llegara):
    print(f"Múltiplos de {multiplo} * {valor} = ", valor * multiplo)