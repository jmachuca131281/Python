dia = int(input(print("Digite el día: ")))
mes = int(input(print("Digite el mes: ")))

#horoscopo = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
#signo = ["null", "capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario"]

def mostrar(a, b, c):
    print(f"Sr Usuario fu Fecha de Cumpleaños es: {dia} de el {mes}")
    print(f"Su signo zodiacal {signo}")

if ((dia >= 22) and (mes == 12)) or ((dia <= 19) and (mes == 1)):
    signo = "Capricornio"
    mostrar("dia", "mes", "signo")

if ((dia >= 20) and (mes == 1)) or ((dia <= 17) and (mes == 2)):
    signo = "Acuario"
    mostrar("dia", "mes", "signo")

if ((dia >= 18) and (mes == 2)) or ((dia <= 19) and (mes == 3)):
    signo = "Piscis"
    mostrar("dia", "mes", "signo")

if ((dia >= 20) and (mes == 3)) or ((dia <= 19) and (mes == 4)):
    signo = "Aries"
    mostrar("dia", "mes", "signo")

if ((dia >= 20) and (mes == 4)) or ((dia <= 20) and (mes == 5)):
    signo = "Tauro"
    mostrar("dia", "mes", "signo")

if ((dia >= 20) and (mes == 4)) or ((dia <= 20) and (mes == 5)):
    signo = "Tauro"
    mostrar("dia", "mes", "signo")

if ((dia >= 21) and (mes == 5)) or ((dia <= 20) and (mes == 6)):
    signo = "Géminis"
    mostrar("dia", "mes", "signo")

if ((dia >= 21) and (mes == 6)) or ((dia <= 22) and (mes == 7)):
    signo = "Cáncer"
    mostrar("dia", "mes", "signo")

if ((dia >= 23) and (mes == 7)) or ((dia <= 22) and (mes == 8)):
    signo = "Leo"
    mostrar("dia", "mes", "signo")

if ((dia >= 23) and (mes == 8)) or ((dia <= 22) and (mes == 9)):
    signo = "Virgo"
    mostrar("dia", "mes", "signo")

if ((dia >= 23) and (mes == 9)) or ((dia <= 22) and (mes == 10)):
    signo = "Libra"
    mostrar("dia", "mes", "signo")

if ((dia >= 23) and (mes == 10)) or ((dia <= 21) and (mes == 11)):
    signo = "Escorpio"
    mostrar("dia", "mes", "signo")

if ((dia >= 22) and (mes == 11)) or ((dia <= 21) and (mes == 12)):
    signo = "Sagitario"
    mostrar("dia", "mes", "signo")
