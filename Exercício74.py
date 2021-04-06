nota1, nota2, nota3, nota4 = float(input()), float(input()), float(input()), float(input())

mean = (nota1 + nota2 + nota3 + nota4)/ 4

if mean >= 7.0:
	print('Aprovado, nota final: {}'.format(mean))
else:
	print('Reprovado, nota final: {}'.format(mean))