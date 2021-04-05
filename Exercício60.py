import math

hora_inicio = int(input())
minuto_inicio = int(input())
hora_termino = int(input())
minuto_termino = int(input())

if minuto_inicio > minuto_termino:
    minuto_inicio = minuto_termino + 60
    hora_termino = hora_termino - 1

if hora_inicio > hora_termino:
    hora_termino = hora_termino + 24

minuto_duracao = minuto_termino - minuto_inicio
hora_duracao = abs(hora_termino - hora_inicio)

print('O jogo durou: {}:{}'.format(hora_duracao, minuto_duracao))