salario, conta1, conta2 = float(input()), float(input()), float(input())

multa1, multa2 = (conta1 * 0.02), (conta2 * 0.02)

salario = salario - (multa1 + multa2)

print('O que restará do salário: %.3f' % salario)