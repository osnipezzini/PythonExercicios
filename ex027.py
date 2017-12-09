"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente .

Ex: Ana Maria de Souza
primeiro = Ana
ultimo =  Souza"""
from format import style
nome = str(input('Digite seu nome completo : ')).strip()
n = nome.split()
style()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
style()
