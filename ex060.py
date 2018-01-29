'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5x4x3x2x1 = 120
'''
from emoji import emojize
user = int(input('Digite um valor e lhe mostrarei o fatorial : '))
mul = user
fat = 1
sign = emojize(':heavy_multiplication_x:', use_aliases=True)
while mul > 0:
    print('{}'.format(mul), end='')
    print(sign if mul > 1 else ' = ', end='')
    fat *= mul
    mul -= 1
print('{}'.format(fat))
