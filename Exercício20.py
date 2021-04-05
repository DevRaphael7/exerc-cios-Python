import math

graus, altura = float(input('Ângulo: ')), float(input())

radiano = math.radians(45)
escada = altura / radiano

print('%.3f' % escada)