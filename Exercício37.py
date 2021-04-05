salario_minimo, salario_func = float(input('Valor do salário mínimo: ')), float(input('Valor do salário do funcionário: '))

quant_salario = salario_func / salario_minimo

print('Quantidade aproximada de salario mínimos que o funcionário recebe:\n{}'.format(round(quant_salario)))
