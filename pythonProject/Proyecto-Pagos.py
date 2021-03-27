numeroMesa = []
plato = []
bebida = []
postre = []
listaPlatos = ["Chuleta en salsa", "Costillas fritas", "Lechona especial", "Chicharron agridulce"]
listaBebidas = ["Batido natural", "Gaseosa", "Vino", "Chicha peruana"]
listaPostres = ["Marquza de chocolate", "Brownie", "Banana Split", "Torta de chocolate"]
preciosPlatos = [3.3, 4.2, 5.6, 6.7]
preciosBebidas = [2.3, 2.4, 5.4, 4.4]
preciosPostres = [1.3, 1.5, 3.2, 2.3]

#def imprimeMesa(plato):
#  for x in plato:
#      r = listaPlatos[x]
#      print(f"El plato es: {r}")
# print(f"Estos son los platos seleccionados: {plato}")

def mesas():
  numeroMesa = int(input(print("Selecciones la mesa a utilizar: 1, 2, 3")))

def factura():
  total = 0
  print("Restaurante el Cochinito feliz\n        Factura de venta")
  print()
  for x in plato:
    r = listaPlatos[x]
    precioPlato = preciosPlatos[x]
    total += precioPlato
    print(f"1 {r}          ..............  $ {precioPlato}")
  for x in bebida:
    r = listaBebidas[x]
    precioBebida = preciosBebidas[x]
    total += precioBebida
    print(f"1 {r}   ............ $ {precioBebida}")
  for x in postre:
    r = listaPostres[x]
    precioPostre = preciosPostres[x]
    total += precioPostre
    print(f"1. {r} ............. $ {precioPostre}")
  print()
  print(f"IVA 19%                    ................. $ 100 ")
  print(f"Total                       .............. $ {total}")
  print()
  print("      Gracias por su compra          ")
  print()
  mesas()

def opciones(menu):
  if menu == 1:
    platos = 0
    while platos != 4:
      platos = int(input(
        print("Por favor, seleccione una de las opciones del menu:"
              "\n0. Chuleta en salsa"
              "\n1. Costillas fritas"
              "\n2. Lechona especial"
              "\n3. Chicarron agridulce"
              "\n4. Salir")))
      if platos <= 3:
        plato.append(platos)
      if platos == 4:
        menuPrincipal()
  elif menu == 2:
    bebidas = 0
    while bebidas != 4:
      bebidas = int(input(
        print("Por favor selecciones una de las opccione del menu:"
              "\n0. Batido natural"
              "\n1. Gaseosa"
              "\n2. Vino"
              "\n3. Chicha Peruana"
              "\n4. Salir")))
      if bebidas <= 3:
        bebida.append(bebidas)
      if bebidas == 4:
        menuPrincipal()
  elif menu == 3:
    postres = 0
    while postres != 4:
      postres = int(input(
        print("Por favor, seleccione una de las opciones:"
              "\n0. Marquza de chocolate"
              "\n1. Brownie"
              "\n2. Banana Split"
              "\n3. Torta de chocolate"
              "\n4. Salir")))
      if postres <= 3:
        postre.append(postres)
      if postres == 4:
        menuPrincipal()
  elif menu == 4:
    print("*** Por favor, agregar los datos del cliente ***")
    nombre = str(input(print("Nombre:")))
    nit = str(input(print("NIT:")))
    telefono = str(input(print("Telefóno: ")))
    cerrarCuenta = int(input(print("Por favor, agregar una opción:\n1. Cancelar\n2. Facturar")))
    if cerrarCuenta == 1:
      menuPrincipal()
    if cerrarCuenta == 2:
      factura()
  elif menu == 5:
    print("Vuelva pronto, muchas gracias...")

def menuPrincipal():
  print("*** Bienvenidos al restaurante el Cochinito Feliz ***")
  menu = int(
    input(print("Por favor, elija una opción:\n1. Platos\n2. Bebidas\n3. Postres\n4. Cerrar cuenta\n5. Salir")))
  opciones(menu)
mesas()
menuPrincipal()