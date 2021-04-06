preco, tipo, refrigeracao = float(input()), input(), input()

if refrigeracao == 'N' and tipo == 'A' and preco < 15.00:
	val_add = 2.00
elif refrigeracao == 'N' and tipo == 'A' and preco >= 15:
	val_add = 5.00
elif refrigeracao == 'N' and tipo == 'L' and preco < 10.00:
	val_add = 1.50
elif refrigeracao == 'N' and tipo == 'L' and preco >= 10.00:
	val_add = 2.50
elif refrigeracao == 'N' and tipo == 'V' and preco < 30.00:
	val_add = 3.00
elif refrigeracao == 'N' and tipo == 'V' and preco >= 30.00:
	val_add = 2.50
elif refrigeracao == 'S' and tipo == 'A':
	val_add = 8.00
elif refrigeracao == 'S' and tipo == 'L':
	val_add = 0.00
elif refrigeracao == 'S' and tipo == 'V':
	val_add = 0.00

if preco < 25.00:
	imp = preco * 0.05
elif preco >= 25.00:
	imp = preco * 0.08

preco_custo = preco + imp

if tipo == 'A' and refrigeracao == 'S':
	preco_custo = preco_custo
else:
	preco_custo = preco_custo - (preco_custo * 0.03)  

new_price = preco_custo + val_add

if new_price <= 50.00:
	print('Barato!')
elif new_price > 50.00 and new_price < 100.00:
	print("Normal")
elif new_price >= 100.00:
	print('Caro')

