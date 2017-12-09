"Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome"
from format import style

nome = str(input('Digite seu nome completo : ')).strip().upper()

style()
print('Seu nome tem Silva ? {}'.format('SILVA' in nome))
style()


