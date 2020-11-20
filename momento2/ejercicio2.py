# Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario.


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

    words = []
    for c,v in dict.items():

        words.append(c)
        words.append(v)

        print(words)

        # print(f'The word "{f}" repeted {v} times')

program(' ')