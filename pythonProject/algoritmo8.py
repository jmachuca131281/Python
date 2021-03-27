promedio = 0
deseaContinuar = "si"
materias = {}
nombreEstudiante = str(input(print("Nombre: ")))
sumatoriaDeNotas = 0
resultado = 0
contador = 0

while deseaContinuar == "si":
    notas = int(input(print("Ingrese la nota")))
    sumatoriaDeNotas += notas
    contador += 1
    materias[str(input(print("Ingrese materia")))] = notas
    deseaContinuar = str(input(print("Desea continuar")))

print(f"El estudiante {nombreEstudiante}")
print(f"Su nota de la materia\n {materias}")
promedio = sumatoriaDeNotas / contador
print(f"El promedio es {promedio}")
