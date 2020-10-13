""" 10) Modificar el algoritmo anterior, de forma que si se teclea un cero, se vuelva a pedir el número por teclado (así hasta que se teclee un número mayor que cero) (recuerda la estructura mientras). """


num = int(input("Digite un numero: "))

intentos = 0

while num < 2:

    num = int(input("Digite un numero numero que no sea 0 ni negativo: "))
    
    if num <= 0:
        intentos += 1
    if intentos == 2:
        print("Muchos intetos, Adios")
        break

if intentos <2:

    if num % 2 == 0:
        print (f"{num} es un numero Par.")
    else:
        print (f"{num} es un numero Impar.")
        