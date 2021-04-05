altura, peso = float(input()), int(input())

if altura < 1.20:
	
	if peso < 60:
		Class = 'A'
	elif peso >= 60 and peso < 90:
		Class = 'D'
	elif peso >= 90:
		Class = 'G'
elif altura >= 1.20 and altura < 1.70:
	
	if peso < 60:
		Class = 'B'
	elif peso >= 60 and peso < 90:
		Class = 'E'
	elif peso >= 90:
		Class = 'H'
elif altura >= 1.70:

	if peso < 60:
		Class = 'C'
	elif peso >= 60 and peso < 90:
		Class = 'F'
	elif peso >= 90:
		Class = 'I'

print('Classe: {}'.format(Class))