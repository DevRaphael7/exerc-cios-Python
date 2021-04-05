print('Digite o código: ');
codigo = int(input());
print('Digite o seu salario: ');
salario = float(input());

if codigo == 1:
	print('Cargo: Escritório');
	percentual = salario * 0.50
	salario = salario + percentual
	print('Novo salário: {} R$'.format(salario))
elif codigo == 2:
	print('Cargo: Secretátio')
	percentual = salario * 0.35
	salario = salario + percentual
	print('Novo salário: {} R$'.format(salario))
elif codigo == 3:
	print('Cargo: Caixa')
	percentual = salario * 0.20
	salario = salario + percentual
	print('Novo salário: {} R$'.format(salario))
elif codigo == 4:
	print('Cargo: Gerente')
	percentual = salario * 0.10
	salario = salario + percentual
	print('Novo salário: {} R$'.format(salario))
elif codigo == 5:
	print('Cargo: Diretor')
	print('Sem aumento: %.2f R$' % salario)