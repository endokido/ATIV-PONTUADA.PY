import os
os.system('cls')

renda_mensal = float(input('Digite sua renda mensal: R$ '))
valor_emprestimo = float(input('Digite o valor total do empréstimo desejado: R$ '))
num_prestacoes = int(input('Digite o número de prestações: '))

limite_emprestimo = renda_mensal * 10
prestacao = valor_emprestimo / num_prestacoes
limite_prestacao = renda_mensal * 0.3


if valor_emprestimo <= limite_emprestimo and prestacao <= limite_prestacao:
    print('Empréstimo concedido!')

elif valor_emprestimo > limite_emprestimo:
    print('Empréstimo negado!')
    print(f'Valor da prestação excede 30% da renda')
elif prestacao > limite_prestacao:
    print('Empréstimo negado!')
    print(f'Valor do empréstimo excede o limite permitido de R$ {limite_emprestimo:.2f}')