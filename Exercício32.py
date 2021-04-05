peso_anterior = float(input())
novo_peso = float(input())

peso_quinze = (peso_anterior * 0.15) + peso_anterior
peso_vinte = peso_anterior - (peso_anterior * 0.20)

if peso_quinze == novo_peso:
    print('Quinze por cento: %.2f' % novo_peso)
elif peso_vinte == novo_peso:
    print('Vinte por cento: %.2f' % novo_peso)