print('Data um: ')
dia1 = int(input())
mes1 = int(input())
ano1 = int(input())
print('Data dois: ')
dia2 = int(input())
mes2 = int(input())
ano2 = int(input())

if ano1 > ano2:
    print('A data um é maior')
else:
    if ano1 != ano2:
        print('A data dois é maior')

if ano1 == ano2:

    if mes1 > mes2:
        print('A data um é maior')
    elif mes1 == mes2:
        if dia1 > dia2:
            print('A data um é maior')
        elif dia1 == dia2:
            print('A data um é igual a data dois')
        else:
            print('A data dois é maior')
    else:
        print('A data dois é maior')