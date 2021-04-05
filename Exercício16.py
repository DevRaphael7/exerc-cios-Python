horas_trabalhadas, salario_mínimo = int(input('Horas trabalhada: ')), float(input('Salário mínimo: '))

h_trab = salario_mínimo / 2.0
s_bruto = horas_trabalhadas * h_trab
imposto = s_bruto % 0.03
s_receber = s_bruto - imposto

print('Número de horas a trabalhar: %.2f ' % h_trab)
print('Salário novo: %.2f' % s_receber)