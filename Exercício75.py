nota1, nota2 = float(input()), float(input())

media = (nota1 + nota2)/2

if media >=0 and media < 3.0:
	print('Reprovado')
elif media >= 3.0 and media < 7.0:
	print('Exame')
elif media >= 7.0 and media <= 10:
	print('Aprovado')
