valor = int(input ('digiteite o valor do produto'))
while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'o valor final do seu produta sera de R${valor}' )
    break