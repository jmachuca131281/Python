vocal = str(input("Ingrese la vocal:"))
a = "a"
e = "e"
i = "i"
o = "o"
u = "u"

if vocal == a or (vocal == e) or (vocal == i) or (vocal == o) or (vocal == u):
    print(f"Si es Vocal\n El caracter ingresado es {vocal}")
else:
    print("El caracter no es una vocal")
