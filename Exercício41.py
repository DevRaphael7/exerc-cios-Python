import math

print('Forneça o valor dos dois catetos do triângulo : ')
cateto_um, cateto_dois = int(input()), int(input())

hipotenusa = math.sqrt((cateto_um ** 2) + (cateto_dois ** 2))

print('Valor da hipotenusa: %f' % hipotenusa)
print('Valor da hipotenusa (valor inteiro): %d' % hipotenusa)
