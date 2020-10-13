""" 11) Algoritmo que nos diga si una persona puede acceder a cursar un ciclo formativo de grado superior o no. Para acceder a un grado superior, si se tiene un titulo de bachiller, en caso de no tenerlo, se puede acceder si hemos superado una prueba de acceso. """

titulo_bach = input("¿Tiene un titulo Bachiller?: (si o no): ")

if titulo_bach == "si" or titulo_bach == "Si":
    print("Puede acceder a un Grado Superior. Bienvenido!")

else:
    prueba_acce=(input("¿Tiene la Prueba de Acceso?"))

    if prueba_acce == "si" or titulo_bach == "Si":
        print("Puede cursar el Grado Superior")

    else:
        print("No puede ingrsar al Grado Superior")