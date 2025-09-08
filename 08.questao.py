import os
os.system('cls')

print("""
Cor         Preço
Verde       R$10,00
Azul        R$20,00
Amarelo     R$30,00
Vermelho    R$40,00

""")

cores = input('Digite a cor desejada (verde, azul, amarelo, vermelho): ')

match cores:
    case 'verde':
        preco = 10.00
    case 'azul':
        preco = 20.00
    case 'amarelo':
        preco = 30.00
    case 'vermelho':
        preco = 40.00

print(f'Preço do CD: {preco}')