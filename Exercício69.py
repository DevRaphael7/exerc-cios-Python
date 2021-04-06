cod_estado, peso_carga, cod_carga = int(input('O código deve ser entre 1 a 5\nCódigo da carga: ')), float(input('Peso em toneladas: ')), int(input('O código da carga deve estar entre 10 a 40:\n'))

conv_kilo = peso_carga * 1000

if cod_carga >= 10 and cod_carga <= 20:
	preco_carga = conv_kilo * 100
elif cod_carga >= 21 and cod_carga <= 30:
	preco_carga = conv_kilo * 250
elif cod_carga >= 31 and cod_carga <= 40:
	preco_carga = conv_kilo * 340

print('Peso da carga em quilos: %.2f' % conv_kilo)
print('Preço da carga: {}'.format(preco_carga))

if cod_estado == 1:
	imposto = preco_carga * 0.35;
elif cod_estado == 2:
	imposto = preco_carga * 0.25;
elif cod_estado == 3:
	imposto = preco_carga * 0.15;
elif cod_estado == 4:
	imposto = preco_carga * 0.05;
elif cod_estado == 5:
	imposto = 'Isento'

print('Valor do imposto: {}'.format(imposto))

v_t = preco_carga + imposto; print('Valor total = {}'.format(v_t))