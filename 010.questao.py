import os
os.system('cls')

print("""
Combustível | Quantidade Vendida | Desconto por litro

Álcool          Até 25 litros                    10%
Álcool          Acima 25 litros                  20%
      
Gasolina        Até 25 litros                    15%
Gasolina        Acima 25 litros                  30%
""")
print('-' * 52)

tipo_combustivel = input('Digite o tipo de combustível: A-álcool ou G-gasolina: ')

match tipo_combustivel:
    case 'A-álcool':
        num_litros = int(input('Digite a quantidade de A-ácool: '))
        
        if num_litros <= 25:
            preco_bruto = (num_litros * 3.79) 
            desconto = (preco_bruto * 0.1)
            total_com_desconto = preco_bruto - desconto

        elif num_litros > 25:
            preco_bruto = (num_litros * 3.79) 
            desconto = (preco_bruto * 0.2)
            total_com_desconto = preco_bruto - desconto
    
    case 'G-gasolina':
        num_litros = int(input('Digite a quantidade de G-gasolina: '))
        if num_litros <= 25:
            preco_bruto = (num_litros * 6.59) 
            desconto = (preco_bruto * 0.15)
            total_com_desconto = preco_bruto - desconto

        elif num_litros > 25:
            preco_bruto = (num_litros * 6.59) 
            desconto = (preco_bruto * 0.3)
            total_com_desconto = preco_bruto - desconto
    case _:
        print('Combustível inválido!')

print('\n')
print("\n==== Combustível ====")
print(f'Tipo de combustível: {tipo_combustivel}')
print(f'Quantide de litros: {num_litros} litros')
print(f'Preço bruto: R${preco_bruto:.2f}')
print(f'Desconto real: R${desconto:.2f}')
print(f'Preço com desconto: R${total_com_desconto:.2f}')
