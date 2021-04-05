import math

print('''
1 - Somar dois números
2 - Raiz quadrada de um número
''')

OP = int(input())

if OP == 1:
    print('Digite dois números em seguida vou somar: ')
    num1 = int(input())
    num2 = int(input())
    print('Resultado do somatório: %d ' % (num1 + num2))
elif OP == 2:
    print('Digite o número para obter sua raiz quadrada:')
    num1 = int(input())
    
    print('Raiz quadrada de {} é {}'.format(num1, math.sqrt(num1)))