from datetime import date
# from datetime import datetime

# today = date.today()
# now = datetime.now()

# print(today)
# print(now)

# print("El dia actual es {}".format(today.day))
# print("El mes actual es {}".format(today.month))
# print("El año actual es {}".format(today.year))


def calcular_edad_años(fecha_nacimiento):
    fecha_actual = date.today()
    resultado = fecha_actual.month - fecha_nacimiento.month

    return resultado

fecha_nacimiento_santo = date(1989, 9, 17)
edad = calcular_edad_años(fecha_nacimiento_santo)

print(f"La edad de santo es: {edad}")

