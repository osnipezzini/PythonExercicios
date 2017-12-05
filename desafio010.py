# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar .

# Considere US$1,00 = R$3,27

n1 = float(input('Quanto você tem de dinheiro ? R$  '))

print('Você pode comprar {:.2f} dólares'.format(n1/3.27))