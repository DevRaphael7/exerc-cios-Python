horas_trabalhada, salario_minimo, horas_extra = int(input()), float(input()), int(input())

horas_trabalhadas = salario_minimo / 8
horas_extras = salario_minimo / 4
s_bruto = horas_trabalhadas * horas_trabalhada
q_hoex = horas_extras * horas_extra
new_salario = q_hoex + s_bruto

print('Salario a receber: %.2f R$' % new_salario)

