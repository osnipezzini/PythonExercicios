# Faça um programa que leia a largura e a altura de uma parede em metros , calcule a sua área e a quantidade de tinta
# necessária para pintá-la , sabendo que cada litro de tinta , pinta uma área de 2m²

n1 = int(input('Qual a largura da parede ? '))
n2 = int(input('Qual a altura da parede ? '))

print('A área total da parede é de {}'.format(n1*n2))
print('Você irá precisar de {} litros de tinta para pintar a parede'.format(n1*n2/2))
