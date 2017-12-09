"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

Ex: Digite um numero: 1834

Unidade:4
Dezena:3
Centena: 8
Milhar: 1"""

from format import style

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
style()
print('Analizando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
style()



