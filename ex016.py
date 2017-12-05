#Crie um programa que leia um número Real qualquer pelo teclado e mostre sua porção inteira
from math import trunc

num = float(input('Digite um valor real: '))
print('O inteiro de {} é {}.'.format(num, trunc(num)))
