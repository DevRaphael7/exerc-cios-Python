nota1, nota2, nota3 = float(input()), float(input()), float(input())

media = (nota1 + nota2 + nota3)/3

if media >= 0.0 and media < 3.0:
    print('Reprovado')
elif media >= 3.0 and media < 7.0:
    print('Exame')
    
    nota_exame = 12 - media

    print('Nota que o aluno deve tirar para ser aprovado %.2f' % nota_exame)
elif media >= 7.0 and media < 10.0:
    print('Aprovado')
