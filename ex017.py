#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo , calcule e mostre o comprimento da hipotenusa.
from math import hypot

cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))

hipo = hypot(cato, cata)

print('A hipotenusa de {} e {} é {:.2f}.'.format(cato, cata, hipo))