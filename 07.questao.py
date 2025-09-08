import os
os.system('cls')

nome_produto = input('Digite o nome do produto: ')
quant_prouto = int(input('Quantidade do produto: '))
preco_unitario = float(input('Preço do produto: '))

if quant_prouto <= 5:
    total = (quant_prouto * preco_unitario)
    desconto = (total * 0.02)
    total_a_pagar = (total - desconto)

elif quant_prouto > 5 and quant_prouto <= 10:
    total = (quant_prouto * preco_unitario)
    desconto = (total * 0.03)
    total_a_pagar = (total - desconto)

elif quant_prouto > 10:
    total = (quant_prouto * preco_unitario)
    desconto = (total * 0.05)
    total_a_pagar = total - desconto

print("\n==== Nota fiscal ====")
print(f'produto: {nome_produto}')
print(f'Valor total: R${total:.2f}')
print(f'Desconto aplicado: R${desconto:.2f}')
print(f'Valor total com desconto: R${total_a_pagar:.2f}')