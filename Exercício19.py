alt_degrau, alt_usuario = float(input('Forneça (em centímetros) a altura dos degrau: ')), float(input('Altura do usuário: '))

quant_degrau = alt_usuario // alt_degrau

print('Quantidade de degraus percorridos: %.0f' % quant_degrau)