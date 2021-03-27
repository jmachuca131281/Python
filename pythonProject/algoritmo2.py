estudiante = str(input("Tipee el nombre del estudiante"))
matematicas = int(input("Ingrese la nota de matematicas"))
español = int(input("Ingrese la nota de español"))
sociales = int(input("Ingrese la nota de sociales"))

print("El estudiante => ", estudiante)
print("La nota de Matematicas es => ", matematicas)
print("La nota de Español es => ", español)
print("La nota de Sociales es => ", sociales)
promedio = (matematicas + español + sociales) / 3
print("Su promdio es => ", promedio)
print("Result with round out: {r:1.1f}".format(r=promedio))