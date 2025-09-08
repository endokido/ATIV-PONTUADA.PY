import os
os.system('cls')

valor_a = int(input('Digite o primeiro valor: '))
valor_b = int(input('Digite o segundo valor: '))
valor_c = int(input('Digite o terceiro valor: '))

soma = (valor_a + valor_b)

print(f'Valor A = {valor_a}')
print(f'Valor B = {valor_b}')
print(f'Valor C = {valor_c}')

if soma > valor_c:
    print(f'O soma de {valor_a} + {valor_b} = {soma} portanto é maior que {valor_c}')
elif soma < valor_c:
    print(f'O soma de {valor_a} + {valor_b} = {soma} portanto é menor que {valor_c}')
else:
    print(f'O resultado da soma {valor_a} + {valor_b} é igual a {valor_c}')


