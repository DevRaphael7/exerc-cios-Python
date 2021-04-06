angulo = int(input('Ângulo: '))

if angulo >= 0 and angulo <= 90:
	print('1° Quadrante')
elif angulo >= 90 and angulo <= 180:
	print('2° Quadrante')
elif angulo >= 180 and angulo <= 270:
	print('3° Quadrante')
elif angulo >= 270 and angulo <= 360:
	print('4° Quadrante')
else:
	print('Esse ângulo está fora do círculo trigonométrico.')