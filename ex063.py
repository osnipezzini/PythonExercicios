'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci.

Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8
'''
from emoji import emojize
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
num = int(input('Digite um número: '))
c1 = 0
c2 = 1
sign = emojize(':arrow_right:', use_aliases=True)
print('~'*30)
print('{} {} {}'.format(c1, sign, c2), end='')
cont = 3
while cont <= num:
    c3 = c1 + c2
    print(' {} {} '.format(sign, c3), end='')
    c1 = c2
    c2 = c3
    cont += 1
print('~'*30)
