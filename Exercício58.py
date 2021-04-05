from datetime import datetime

now = datetime.now()

dia, mes, ano = int(input('Dia:\t')), int(input('Mês:\t')), int(input('Ano:\t'))
hora, minuto = int(input('Hora:\t')), int(input('Minuto:\t'))

print('\n')
print('%02d/%02d/%02d' % (dia, mes, ano))
if mes == 1:
    print('Mês de Janeiro')
elif mes == 2:
    print('Mês de Fevereiro')
elif mes == 3: 
    print('Mês de Março')
elif mes == 4:
    print('Mês de Abril')
elif mes == 5:
    print('Mês de Maio')
elif mes == 6:
    print('Mês de Junho')
elif mes == 7:
    print('Mês de Julho')
elif mes == 8:
    print('Mês de Agosto')
elif mes == 9:
    print('Mês de Setembro')
elif mes == 10:
    print('Mês de Outubro')
elif mes == 11:
    print('Mês de Novembro')
elif mes == 12:
    print('Mês de Dezembro')

print('{}:{}'.format(hora, minuto))

print('\nData e hora do sistema operacional:')
print ('{}:{}:{}'.format(now.hour, now.minute, now.second))