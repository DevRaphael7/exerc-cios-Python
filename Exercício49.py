hora, minuto = int(input('Horas: ')), int(input('Minutos: '))

horas_para_minutos = hora * 60
Minutos_totais = horas_para_minutos + minuto
segundos = Minutos_totais * 60

print('Horas para minuto: {}'.format(horas_para_minutos))
print('Minutos totais: {}'.format(Minutos_totais))
print('Minutos totais para segundos: {}'.format(segundos))
