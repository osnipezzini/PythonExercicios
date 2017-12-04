# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

n1 = int(input('Digite seu atual sálario : '))
resultado = n1*15/100

print('Seu novo salário é de : {}'.format(resultado+n1))