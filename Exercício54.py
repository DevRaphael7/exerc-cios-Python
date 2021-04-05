print('Digite três números em ordem crescente:')
print('Número um:'); numero1 = int(input())
print('Número dois: '); numero2 = int(input())
print('Número três: '); numero3 = int(input())
print('Digite mais um número sem ordem:')
print('Número quatro: '); numero4 = int(input())

if numero4 > numero3 and numero4 > numero2 and numero4 > numero1:
    print('{}, {}, {}, {}'.format(numero4, numero1, numero2, numero3))
elif numero4 < numero3 and numero4 < numero2 and numero4 < numero1:
    print('{}, {}, {}, {}'.format(numero1, numero2, numero3, numero4))
elif numero4 > numero3 and numero4 < numero2 and numero4 < numero1:
    print('{}, {}, {}, {}'.format(numero1, numero2, numero4, numero3))
elif numero4 > numero3 and numero4 > numero2 and numero4 < numero1:
    print('{}, {}, {}, {}'.format(numero1, numero4, numero2, numero3))