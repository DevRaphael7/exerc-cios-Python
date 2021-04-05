print('Digite o número um: ')
numero1 = int(input())
print('Digite o número dois: ')
numero2 = int(input())
print('Digite o número três: ')
numero3 = int(input())

if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
    print('{}, {}, {}'.format(numero3, numero2, numero1))
elif numero1 < numero2 and numero1 > numero3 and numero2 > numero3:
    print('{}, {}, {}'.format(numero3, numero1, numero2))
elif numero1 < numero2 and numero1 < numero3 and numero2 > numero3:
    print('{}, {}, {}'.format(numero1, numero3, numero2))
elif numero1 > numero2 and numero1 > numero3 and numero2 < numero3:
    print('{}, {}, {}'.format(numero2, numero3, numero1))
elif numero1 < numero2 and numero1 < numero3 and numero2 < numero3:
    print('{}, {}, {}'.format(numero1, numero2, numero3))
elif numero1 > numero2 and numero1 < numero3 and numero2 < numero3:
    print('{}, {}, {}'.format(numero2, numero1, numero3))