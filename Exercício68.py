codigo_prod, peso, codigo_pais = int(input()), int(input()), int(input())

kilos_gramas = peso * 1000; print('Gramas do peso: {}'.format(kilos_gramas))

if codigo_prod >= 1 and codigo_prod <= 4:
	preco = kilos_gramas * 10;
elif codigo_prod >= 5 and codigo_prod <= 7:
	preco = kilos_gramas * 25
elif codigo_prod >= 8 and codigo_prod <= 10:
	preco = kilos_gramas * 35

if codigo_pais == 1:
	imposto = 0
elif codigo_pais == 2:
	imposto = (preco * 0.15) + preco
elif codigo_pais == 3:
	imposto = (preco * 0.25) + preco

valor_total = preco + imposto

print('Valor total: {}'.format(valor_total))