import random

def run():
    numero_aleatorio= random.randint(1, 100)
    numero_elegido = int(input('Elige un Número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Bucas un numero mayor')
        else:
            print('Buca un numero pequeño')
        numero_elegido = int(input('Elige otro número: ') )
    print('!Ganaste careguanabana')


if __name__=='__main__':
    run()
import random

