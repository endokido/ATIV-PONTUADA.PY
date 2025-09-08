import os
os.system('cls')

num_a = int(input('Digite o primeiro número: '))
operadores = input('Digite os operadores (+, - * ou /): ')
num_b = int(input('Digite o segundo número: '))

resultado = 0

match operadores:
    case '+':
        resultado = num_a + num_b
        print(f'O resulado de {num_a} {operadores} {num_b} = {resultado}')
    case '-':
        resultado = num_a - num_b
        print(f'O resulado de {num_a} {operadores} {num_b} = {resultado}')
    case '*': 
        resultado = num_a * num_b
        print(f'O resulado de {num_a} {operadores} {num_b} = {resultado}')
    case '/':
        if num_a != 0 or num_b != 0:
            print('Não é possível dividir por zero!')
        else:
            resultado = num_a / num_b
            print(f'O resulado de {num_a} {operadores} {num_b} = {resultado}')
    case _:
        print('Operador inválido')


