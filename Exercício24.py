horas = float(input())

horas_int = int(horas)
minutos_float = round(horas - int(horas), 2)
conversao = (horas * 60) + (minutos_float * 100)

print('%.0f' % conversao)