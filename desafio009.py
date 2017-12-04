# Faça um programa que leia um número inteiro qualquer e mostra na tela a sua tabuada.

n1 = int(input('Digite um número : '))

contador = 1

while contador <= 10:
    print('{} X {} = {}'.format(n1, contador, n1*contador))
    contador= contador + 1