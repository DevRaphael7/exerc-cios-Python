print('Digite a nota pelo trabalho de laboratório: ')
trab_lab = float(input())
print('Digite a nota pela avaliação semestral: ')
aval_sems = float(input())
print('Digite a nota pelo exame final: ')
exam_final = float(input())

nota_final = ((trab_lab * 2) + (aval_sems * 3) + (exam_final * 5))/10

print('Nota final: %.2f' % nota_final)

if nota_final >= 8.0 and nota_final <= 10.0:
    print('Conceito A')
elif nota_final >= 7.0 and nota_final < 8.0:
    print('Conceito B')
elif nota_final >= 6.0 and nota_final < 7.0:
    print('Conceito C')
elif nota_final >= 5.0 and nota_final < 6.0:
    print('Conceito D')
elif nota_final >= 0.0 and nota_final < 5.0:
    print('Conceito E')

