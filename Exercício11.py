import math 
#Exercício 11 da página 42



num = float(input('Digite um número: '))

print('Número ao quadrado: {}\nNúmero ao cubo: {}'.format(num ** 2, num ** 3))
print('Raiz quadrada: %.4f\nRaiz cúbica: %.4f' % (math.sqrt(num), num ** (1/3)) )