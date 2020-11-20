# Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
# scort= ordena de mayor a menor
#append agrega el numero a la lista
numberList = []
 
salir = False
 
print(' ')
print("************ Welcome to pick up numbres ***************")
print(' ')

while(not salir):
    numero = int(input("Dame un numero: "))
    if(numero == 0):
        salir=True
    else:
        numberList.append(numero)
 
numberList.sort() 
 
print(numberList)