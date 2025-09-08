import os
os.system('cls')

valor_a = int(input('Digite o primeiro valor: '))
valor_b = int(input('Digite o segundo valor: '))

if valor_a == valor_b:
    soma = valor_a + valor_b
    valor_c = soma
    print(f'Resultado da soma: {valor_c}')
else:
    produto = valor_a * valor_b
    valor_c = produto
    print(f'Resultado do produto: {valor_c}')

