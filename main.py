import pandas  

# TODO 1. Creando un diccionario a partir de nuestro archivo CSV externo
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# Crea un diccionario a partir de los datos del CSV, asignando a cada letra su código fonético correspondiente
data_dictionary = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


# print(data_dictionary)

# TODO 2. El usuario ingresa una palabra y el programa debe deletrearla correctamente
sentence = input("Ingrese una palabra que desee ver deletreada utilizando el alfabeto de la OTAN: ")

# Convierte la entrada a mayúsculas para garantizar consistencia
capital_letters = sentence.upper()

# Crea una lista de códigos fonéticos correspondientes a cada letra en la palabra ingresada
lista_de_palabras = [data_dictionary[letter] for letter in capital_letters if letter in data_dictionary]

# Imprime la lista de códigos fonéticos
print(lista_de_palabras)
