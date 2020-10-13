""" 7) Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el curso actual. Diseñar un algoritmo para este propósito (recuerda que para calcular el porcentaje puedes hacer una regla de 3). """



numero_niños = (int(input("Escrita la cantidad de niños: ")))
numero_niñas = (int(input("Escrita la cantidad de niñas: ")))


porcentaje_niños = numero_niños*100/ (numero_niños + numero_niñas)
porcentaje_niñas = 100-porcentaje_niños

print(f"El porcentade de  niños es {porcentaje_niños}%")
print(f"El porcentade de  niños es {porcentaje_niñas}%")



