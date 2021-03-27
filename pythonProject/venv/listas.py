color = ['red', 'pink', 'blue', 'orange']
color.append('black')
for c in color:
    print(c)

# Diccionarios
diccionario_colores = {"red":"ping", "blue":"grey", "black":"red"}
print(diccionario_colores)
diccionario_colores["red"]
print(diccionario_colores["red"])

diccionario_colores["yellow"] = "amarillo"
print(diccionario_colores)
blue = diccionario_colores.pop("blue")
print(blue)
del(diccionario_colores["black"])
print(diccionario_colores)

for clave, valor in diccionario_colores.items():
    print(clave, valor)

diccionariDeMaterias = {}
diccionariDeMaterias["matematicas"] = 3
print(diccionariDeMaterias)


 