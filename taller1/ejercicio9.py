""" 9) Realizar un algoritmo que dado un número entero, visualice en pantalla si es par o impar. En el caso de ser 0, debe visualizar “el número no es par ni impar” (para que un numero sea par, se debe dividir entre dos y que su resto sea 0) """

num = int(input("Digite un numero: "))


if num % 2 == 0:
    print (f"{num} es un numero Par.")
else:
    print (f"{num} es un numero Impar.")
    