'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    num = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano - num >= 21:
        maior += 1
    else:
        menor += 1
print('Tivemos um total de {} pessoas maiores de idade e {} pessoas menores de idade'.format(maior, menor))
