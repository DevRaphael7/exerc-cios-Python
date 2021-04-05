sal_minimo, quilowatt = float(input()), float(input())

valor_quilowatt = sal_minimo / 5
valor_quilowatt_pago = quilowatt * valor_quilowatt
val_pago = sal_minimo - (sal_minimo * 0.15)

print('Valor do quilowatt: %.2f' % valor_quilowatt)
print('Quantidade de quilowatt: %.2f' % valor_quilowatt_pago)
print('Valor a ser pago com desconto de quinze por cento: %.2f' % val_pago)