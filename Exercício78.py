numeroUm, numeroDois = int(input('Numero um: ')), int(input('Numero dois: '))

OP = int(input("Escolha uma opção entre 1 a 4: "))

if OP == 1:
	operacao = (numeroUm + numeroDois)/2
elif OP == 2:
	if numeroUm > numeroDois:
		operacao = numeroUm - numeroDois
	else:
		operacao = numeroDois - numeroUm
elif OP == 3:
	operacao = numeroUm * numeroDois
elif OP == 4:
	operacao = numeroUm / numeroDois
else:
	print('Digite uma das opções de 1 a 4\n')
	operacao = 0

print('Resultado: %.2f' % operacao)