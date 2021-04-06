numeroUm, numeroDois, numeroTres = int(input('Número um: ')), int(input('Número dois: ')), int(input('Número três: '))

if numeroUm > numeroDois and numeroDois > numeroTres:
	print('Número {} é maior'.format(numeroUm))
elif numeroUm < numeroDois and numeroDois > numeroTres:
	print('Número {} é maior'.format(numeroDois))
elif numeroUm < numeroDois and numeroDois < numeroTres:
	print('Número {} é maior'.format(numeroTres))