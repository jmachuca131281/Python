numero1 = int(input("Add frist number"))
numero2 = int(input("Add second number"))

suma = (numero1 + numero2)
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
print(f"Suma entre {numero1} y {numero2} is: ", suma)
print(f"Resta entre {numero1} y {numero2} is: ", resta)
print(f"Division entre {numero1} y {numero2} is: ", division)
print("Result with round out: {r:1.3f}".format(r=division))
print(f"Multiplicación entre  {numero1} y {numero2} is: ", multiplicacion)
