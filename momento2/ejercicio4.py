# Hacer una actividad que pida al usuario escribir una cantidad X de nombres de personas (puede hacerlo con el ciclo que considere). Después el sistema deberá demostrar cuales son los nombres que empiezan con la letra "C" sea minúscula o mayúscula.



names = []
namesC = []

print(' ')
print("************ Welcome to C Names Counter ***************")
print(' ')

print('Type 5 names: ')
for i in range(5):
    name = (input())
    names.append(name)


for n in names:
    if n[0] == 'C' or n[0] == 'c':
        namesC.append(n)

print(namesC)



