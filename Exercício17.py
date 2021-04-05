salario, cheque1, cheque2 = float(input('Seu salário: ')), float(input('Seu cheque um: ')), float(input('Seu cheque dois: '))

v_cheque1, v_cheque2 = cheque1 * 0.38, cheque2 * 0.38
saldo = salario - cheque1 - cheque2 - v_cheque1 - v_cheque2
print(saldo)