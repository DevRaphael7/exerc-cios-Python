numeroUm, numeroDois, numeroTres = int(input()), int(input()), int(input())

if numeroUm > numeroDois and numeroDois > numeroTres:
	print('Número {} é maior'.format(numeroUm))
elif numeroUm < numeroDois and numeroDois > numeroTres:
	print('Número {} é maior'.format(numeroDois))
elif numeroUm < numeroDois and numeroDois < numeroTres:
	print('Número {} é maior'.format(numeroTres))