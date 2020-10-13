""" 4) Algoritmo que lea tres números distintos y nos diga cual de ellos es el mayor (recuerda usar la estructura condicional Si y los operadores lógicos). """


num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))


if num1 > num2 and num1 > num3:
    print(f"{num1} es mayor que {num2} y {num3}")

elif num2 > num1 and num2 >num3:
    print(f"{num2} es mayor que {num1} y {num3}")

elif num3 > num1 and num3 > num2:
    print(f"{num3} es mayor que {num1} y {num2}")




    

