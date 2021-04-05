X, Y, Z = int(input()), int(input()), int(input())

if X < Y + Z and Y < X + Z and Z < X + Y:

	if X == Y and Y == Z:
		print('Triângulo equilátero')
	elif X == Y or Y == Z or X == Z:
		print('Triângulo isóceles')
	elif X != Y and Y != Z and X != Z:
		print('Triângulo escleno')
else:
	print('Estas medidas não formam um triângulo')