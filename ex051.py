'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
from emoji import emojize
num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
dez = num + (10 - 1) * raz
sign = emojize(':arrow_right:', use_aliases=True)
for c in range(num, dez, raz):
    print('{} {} '.format(c, sign), end=' ')
print('ACABOU')