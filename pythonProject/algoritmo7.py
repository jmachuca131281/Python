import os
x = "si"
while x == "si":
    valorIncial = int(input(print("Señor usuario digite el número inicio")))
    valorFinal = int(input(print("Señor usuairo digite el núnero final")))
    intervalo = int(input(print("Señor usuario digite el número intervalo")))
    x = str(input(print("Desea continuar")))
    if x == "no":
        print("Muchas gracias")
    print(f"ValorIncial {valorIncial}, Valor final {valorFinal} y el Intervalo {intervalo}")