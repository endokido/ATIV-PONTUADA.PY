import os
os.system('cls')

nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))

media = (nota_1 + nota_2) / 2

if media >= 6.0:
    print(f'Sua média é {media}')
    print('Parabéns, você está aprovado!')
elif media >= 4.1 and media <= 5.9:
    print(f'Sua média é {media}')
    print('Recuperação')
elif media < 4.0:
    print(f'Sua média é {media}')
    print('Você está reprovado!')
