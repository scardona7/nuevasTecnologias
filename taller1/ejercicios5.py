""" 5) Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo, debe imprimir el producto de los tres y si no lo es, imprimirá la suma. """


num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

producto= -num1 * num2 * num3
suma = num1 + num2 + num3

if num1 <0:
    print(producto)

else:
    print(suma)
    