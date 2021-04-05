import math

tam_esca = int(input())
altura = int(input())

distancia = (tam_esca ** 2) - (altura ** 2)
distancia = (math.sqrt(distancia))

print(distancia)