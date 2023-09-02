# FOR LOOP - IF ELSE
compra_confirmada = True
dados_compa = 'compra no valor de R$12,50 e entrega confirmada'

for enviar in range(3):
  if compra_confirmada:
    print(dados_compa)
    print('Detalhes enviados para o seu email')
    break
  else:
    print('falha na compra')