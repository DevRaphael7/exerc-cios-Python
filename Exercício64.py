sal_minimo, h_trabalhada, n_dependentes, horas_extras = float(input('Salário mínimo: ')), int(input('Horas trabalhadas: ')), int(input('Número de dependentes: ')), int(input('Horas extras: '))

h_trabalhadas = sal_minimo/5
sal_mensal = h_trabalhadas * h_trabalhada
numero_dependentes = n_dependentes * 32
horas_extras = (horas_extras * 0.50) * horas_extras
s_bruto = sal_mensal + numero_dependentes + horas_extras

if s_bruto < 200:
	imposto = 0
elif s_bruto >= 200 or s_bruto < 500:
	imposto = s_bruto * 0.10
elif s_bruto >= 500:
	imposto = s_bruto * 0.20; 

salario_liquido = s_bruto - imposto

if salario_liquido < 350:
	gratificacao = 100
else:
	gratificacao = 50

salario_receber = salario_liquido + gratificacao

print('Salario a receber: {} R$'.format(salario_receber))