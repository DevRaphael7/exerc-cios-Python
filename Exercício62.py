op = int(input())

if op == 1:
	print('Seu salario: ')
	salario = float(input())
	if salario <= 500:
		imposto = (salario * 0.05) + salario
	elif salario > 500 or salario <= 850:
		imposto = (salario * 0.10) + salario
	elif salario > 850:
		imposto = (salario * 0.15) + salario
	print('Imposto: %.2f R$' % imposto)
elif op == 2:
	print('Seu salario: ')
	salario = float(input())
	if salario >= 1500:
		new_salary = salario + 25
	elif salario >= 750 or salario < 1500:
		new_salary = salario + 50
	elif salario >= 450 or salario < 750:
		new_salary = salario + 75
	elif salario < 450:
		new_salary = salario + 100
	print('Seu novo salario: {}'.format(new_salary))
elif op == 3:
	print('Seu salario: ')
	salario = float(input())
	if salario < 700:
		print('Mal remunerado')
	elif salario >= 700:
		print('Bem remunerado')
elif op != 1 or op != 2 or op != 3:
	print('Digite uma das opções acima')