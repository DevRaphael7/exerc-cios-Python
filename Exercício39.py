ano_nascimento, ano_atual = int(input()), int(input())

idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dia = idade_anos * 365
idade_semana = idade_dia * 52.1428571

print('Idade em anos: %d' % idade_anos)
print('Idade em meses: %d' % idade_meses)
print('Idade em dias: %d' % idade_dia)
print('Idade em semanas: %d' % idade_semana)