preco_atual, venda_media = float(input('Preço atual: ')), int(input('Venda média: '))

if venda_media < 500 and preco_atual < 30.00:
	novo_preco = (preco_atual * 0.10) + preco_atual

elif (venda_media >= 500 and venda_media < 1200) and (preco_atual >= 30.00 and preco_atual < 80):
	novo_preco = (preco_atual * 0.15) + preco_atual
elif venda_media >= 1200 and preco_atual >= 80.00:
	novo_preco = preco_atual - (preco_atual * 0.20)  
else:
	novo_preco = 0
print('Novo preço: {}'.format(novo_preco))