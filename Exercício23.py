numero = float(input())

print('Parte inteira do número: %.0f' % numero)
print('Parte fracionária do número: %f' % (numero - int(numero)))
print('Arredondamento do número: {}'.format(round(numero, 3)))