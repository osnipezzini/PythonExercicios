'''
Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
from emoji import emojize
num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
sign = emojize(':arrow_right:', use_aliases=True)
c = 1
while c <= 10:
    print('{} {} '.format(num, sign), end='')
    num += raz
    c += 1
print('ACABOU')
