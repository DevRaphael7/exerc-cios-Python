salario = float(input('Salario do funcionário: '))

if salario < 500:
	novo_salario = (salario * 0.05) + salario
elif salario >= 500 or salario < 1200:
	novo_salario = (salario * 0.12) + salario
	if salario < 600:
		aux_escolar = 150
		print('Auxílio escolar: %.2f R$' % aux_escolar)
		novo_salario += aux_escolar
	elif salario > 600:
		aux_escolar = 100
		print('Auxílio escolar: %.2f R$' % aux_escolar)
		novo_salario += aux_escolar
elif salario > 1200:
	print('Sem bonificação')

print('Novo salario: %.2f R$' % novo_salario)
