from format import style

"""Crie um programa que leia o nome completo de uma pessoa e mostre :

- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo( sem considerar espaços)
- Quantas letras tem o primeiro nome"""

nome = str(input('Digite um nome : ')).strip()
style()
print('O nome em maisculo é : {}'.format(nome.upper()))
print('O nome em minúsculo é : {}'.format(nome.lower()))
print('O nome digitado tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('O primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu nome é {} e ele tem {} letras.'.format(separa[0],len(separa[0])))
style()