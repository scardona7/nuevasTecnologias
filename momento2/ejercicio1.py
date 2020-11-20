# Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy':  c = clave v = value w = word


print(' ')
print("************ Welcome to Words Counter ***************")
print(' ')

def program(phrase):

    dict = {}
    phrase = input("Please, Type a phrase: ")
    

    wordList=phrase.split(" ")

    for w in wordList:

        if w in dict:

            dict[w]+=1

        else:

            dict[w]=1	


    for c,v in dict.items():

        print(f'The word "{c}" repeted {v} times')

program(' ')