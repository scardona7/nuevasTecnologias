""" 8) Una tienda ofrece un descuento del 15% sobre el total de la compra durante el mes de octubre. Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar al cliente. """

importe = float(input("Digite el importe: "))
mes = input("Escriba el mes: ")

if ( mes == "octubre" or mes == "Octubre"):

    total = importe*0.85
    print (f"La cantidad total es de: ${total}")

else:
    total = importe 
    print (f"La cantidad total es de: ${total}")

