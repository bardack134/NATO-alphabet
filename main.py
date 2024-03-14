import pandas  

# TODO 1. Creando un diccionario a partir de nuestro archivo CSV externo
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# Crea un diccionario a partir de los datos del CSV, asignando a cada letra su código fonético correspondiente
phonetic_dictionary = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
# print(phonetic_dictionary)


# TODO 2. El usuario ingresa una palabra y el programa debe deletrearla correctamente


def calcular_phonetic_sound():
    sentence = input("Ingrese una palabra que desee ver deletreada utilizando el alfabeto de la OTAN: ")
    # Convierte la entrada a mayúsculas para garantizar consistencia
    word = sentence.upper()

    # Crea una lista de códigos fonéticos correspondientes a cada letra en la palabra ingresada
    try:
        lista_de_palabras = [phonetic_dictionary[letter] for letter in word ]
        # Imprime la lista de códigos fonéticos
        print(lista_de_palabras)
    except KeyError:
        print('Sorry, only letters in the alfabet please')
        # sente ce = input("Ingrese una palabra que desee ver deletreada utilizando el alfabeto de la OTAN: ")
        calcular_phonetic_sound()
     
calcular_phonetic_sound()        
