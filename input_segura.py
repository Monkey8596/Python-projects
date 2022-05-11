
def primera_letra (lista_palabras):
    primera_letras = []

    for palabra in lista_palabras:
        try: 
            assert type(palabra) == str, ' is not a str'
            assert len(palabra) > 0, ' is not allow str empty '

            primera_letras.append(palabra)

        except AssertionError as e:
            print(e)

    return primera_letras

lista = ['perro', 8, 5.5, '']

print(lista)

print (primera_letra(lista))