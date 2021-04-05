#Exercício 15 página 44 

preco_carro, percentual, percentual_imposto = float(input()), float(input()), float(input())

percentual_do_distribuidor = preco_carro * (percentual/100)
percentual_do_imposto = preco_carro * (percentual_imposto/100)
v_total = preco_carro + percentual_do_distribuidor + percentual_do_imposto

print('Valor do distribuidor: %.2f' % percentual_do_distribuidor)
print('Valor do imposto: %.2f' % percentual_do_imposto)
print('Valor total: %.2f' % v_total)
