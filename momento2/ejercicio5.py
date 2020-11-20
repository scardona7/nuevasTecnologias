# Realice una FUNCIÓN en Python que calcule el índice de masa corporal de una persona y diga el estado en que se encuentre. Debe recibir los parámetros necesarios.
print(' ')
print('----------------Welcome to IMC Program------------------')
print(' ')

def imc(height, weight):

    return weight / height**2


weight = float(input('Write your weight: '))
height = float(input('Write your height: '))

i = imc(height, weight)


print(' ')
print('************ Tabla de IMC*****************')
print('< 18.5 = Peso insuficiente\n18.5 - 24.9 = Normopeso\n25 - 26.9 = Sobrepeso grado I\n27 - 29.9 = Sobrepeso grado II\n30 - 34.9 = Obesidad tipo I\n35 - 39.9 = Obesidad tipo II\n40 - 49.9 = Obesidad tipo III\n> 50 = Obesidad tipo IV')
print(' ')
print('******************************************')
print(' ')

print('Please, compare with the table')
print(f'Your IMC is: {i:.3} ')



