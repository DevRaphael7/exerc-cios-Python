#Exercício 14 do livro de Algoritmo

var1, var2 = int(input('Ano atual: ')), int(input('Ano nascimento: '))

anos = var1 - var2
anos_em2050 = 2050 - var2

print('Sua idade: %d' % (anos))
print('Sua idade em 2050: %d' % (anos_em2050))