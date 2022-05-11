pesos = input('Pesos Colombianos: ')
pesos = float(pesos)
valor_dolar=3776.12
dolares= pesos/valor_dolar
dolares=round(dolares, 2)
dolares=str(dolares)
print( 'Tienes $' + dolares + ' dolares')
