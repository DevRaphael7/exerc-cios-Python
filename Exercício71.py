sal_min, turno, horas_trab, categoria = float(input()), input(), int(input()), input()

if turno == 'M':
	coeficiente = sal_min * 0.10
elif turno == 'V':
	coeficiente = sal_min * 0.15
elif turno == 'N':
	coeficiente = sal_min * 0.12

sal_bruto = horas_trab * coeficiente

if categoria == 'O' and sal_bruto >= 300.00:
	imp = sal_bruto * 0.05
elif categoria == 'O' and sal_bruto < 300.00:
	imp = sal_bruto * 0.03
elif categoria == 'G' and sal_bruto >= 400.00:
	imp = sal_bruto * 0.06
elif categoria == 'G' and sal_bruto < 400.00:
	imp = sal_bruto * 0.04

if turno == 'N' and horas_trab > 80:
	grat = 50
else:
	grat = 30

if categoria == 'O' and coeficiente <= 25:
	aux_alimentacao = sal_bruto/4
else:
	aux_alimentacao = sal_bruto/2

salario_liquido = sal_bruto - imp + grat + aux_alimentacao

if salario_liquido < 350.00:
	print('Mal remunerado')
elif salario_liquido >= 350 and salario_liquido < 600:
	print('Normal')
elif salario_liquido >= 600:
	print('Bem remunerado')