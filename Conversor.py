
def conversor(tipo_pesos, valor_dolar):
    pesos = input('Pesos '+ tipo_pesos + ':')
    pesos = float(pesos)
    dolares= pesos/valor_dolar
    dolares=round(dolares, 2)
    dolares=str(dolares)
    print( 'Tienes $' + dolares + ' dolares')


menu= '''
Bienvenido al Conversor de monedas :)

1 - Pesos colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elije una opcion: '''

opcion=int (input(menu))

if opcion == 1:
    conversor('Colombianos ', 3875)
elif opcion == 2:
    conversor('Argentinos ', 65)
elif opcion == 3:
    conversor('Mexicanos ', 24)
else:
    print('Ingrese un numero correcto careguanabana')