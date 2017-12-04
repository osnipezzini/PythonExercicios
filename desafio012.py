# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

n1 = int(input('Digite o preço antigo do produto '))
percentual = n1*5/100
print('O novo preço com 5% de desconto é {}'.format(n1 - percentual))
