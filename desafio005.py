# Faça um programa que leia um número inteiro e mostre na tela o seu número anterior e seu numero depois.

n1 = int(input('Digite um número : '))

print("O número antecessor de {} é : {}".format(n1, n1 - 1))
print('O número posterior a {} é : {}'.format(n1, n1 + 1))
