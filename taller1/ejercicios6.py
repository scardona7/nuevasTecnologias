""" Realizar un algoritmo que lea un número por teclado. En caso de que ese número sea 0 o menor que 0, se saldrá del programa imprimiendo antes un mensaje de error. Si es mayor que 0, se deberá calcular su cuadrado y la raiz cuadrada del mismo, visualizando el numero que ha tecleado el usuario y su resultado (“Del numero X, su potencia es X y su raiz X” ). Para calcular la raiz cuadrada se puede usar la función interna RAIZ(X) o con una potencia de 0,5. """


import math
num = int(input("Digite un numero numero: "))

intentos = 0

while num < 2:

    num = int(input("Digite un numero numero: "))
    
    if num < 0:
        intentos += 1
    if intentos == 2:
        print("Muchos intetos, Adios")
        break

if intentos < 2:

    potencia = num**2
    raiz = math.sqrt(num)

    print(f"El resultado de la potencia es: {potencia}\nLa raiz cuadrada de {num} es {raiz}")




