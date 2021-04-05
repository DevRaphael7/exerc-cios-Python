peso_saco, saco_gato1, saco_gato2 = int(input()), int(input()), int(input())

saco_gato1, saco_gato2 = saco_gato1 / 1000, saco_gato2 / 1000
p_total = peso_saco - 5 * (saco_gato1 + saco_gato2)

print('Quantidade total: %d' % p_total)