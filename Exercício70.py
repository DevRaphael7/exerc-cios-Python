salario, tempo = float(input('Salario: ')), int(input('Tempo de serviço: '))

if salario < 200.00:
	imp = 'Isento'
elif salario >= 200 and salario < 450.00:
	imp = salario *0.03
elif salario >= 450.00 and salario < 700.00:
	imp = salario * 0.08
elif salario >= 700.00:
	imp = salario * 0.12

if salario > 500.00 and tempo <= 3:
	grat = 20;
elif salario > 500 and tempo >= 3:
	grat = 30;
elif salario < 500.00 and tempo < 3:
	grat = 23; 
elif salario < 500 and (tempo >= 3 and tempo < 6):
	grat = 35;
elif salario < 500 and tempo > 6:
	grat = 33;

salario_liquido = salario - imp + grat

if salario_liquido < 350.00:
	print('Classificação: A')
elif salario_liquido >= 350.00 and salario_liquido < 600.00:
	print('Classificação: B')
elif salario_liquido >= 600.00:
	print('Classificação: C')

