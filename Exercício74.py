nota1, nota2, nota3, nota4 = float(input('Digite a nota 1: ')), float(input('Digite a nota 2: ')), float(input('Digite a nota 3: ')), float(input('Digite a nota 4: '))

mean = (nota1 + nota2 + nota3 + nota4)/ 4

if mean >= 7.0:
	print('Aprovado, nota final: {}'.format(mean))
else:
	print('Reprovado, nota final: {}'.format(mean))