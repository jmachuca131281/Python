cantidad = int(input(print("Sr. usuario cuanto familiares tiene: ")))

for x in range(0, cantidad):
    nombreFamilia = str(input(print(f"Sr. usuario digite los nombres del {x} familiar: ")))
    apellidoFamilia = str(input(print(f"Sr. usuario digite los apellido del {x} familiar: ")))
    telefonoFamilia = str(input(print(f"Sr. usuario digite los telefono del {x} familiar: ")))
    fechaCumpleaños = str(input(print(f"Sr. usuario digite los fecha del {x} familiar: ")))
    print(f"Sr usuario su {x} familiar es: {nombreFamilia } { apellidoFamilia}\nSu teléfono es {telefonoFamilia} y el cumpleaños es {fechaCumpleaños}\n ")

