import os
os.system('cls')

print('TABELA DE PREÇOS')
print('-'*40)
print("""
Fruta	    Até 5 Kg	   Acima de 5 Kg

Morango	    R$2,50 por Kg  R$2,20 por Kg
Maçã	    R$1,80 por Kg  R$1,50 por Kg
""")
print('-'*40)

quant_morangos = float(input('Quantos kg de morangos? '))
quant_macas = float (input('Quantos kg de mançãs? '))

if quant_morangos <= 5: 
    valor_morangos = quant_morangos * 2.50
else:
    valor_morangos = quant_morangos * 2.20

if quant_morangos <= 5: 
    valor_macas = quant_macas * 1.80
else:
    valor_macas = quant_macas * 1.50

valor_total = valor_morangos + valor_macas

if quant_morangos + quant_macas >= 10 or valor_total > 15:

    desconto = (valor_total * 0.1)
    valor_com_desconto = valor_total - desconto

    print(f'Valor total da compra: R${valor_total}')
    print(f'Desconto real: {desconto:.2f}')
    print(f'O valor total da compra com desconto de 10% é de R${valor_com_desconto:.2f}')
else:
    desconto = (valor_total * 0.1)
    print(f'Valor total da compra: R${valor_total}')
    print(f'Desconto real: {desconto:.2f}')
    print('Desconto não se aplica')

    


