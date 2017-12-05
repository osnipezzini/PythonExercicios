# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

n1 = float(input('Digite seu atual sálario : '))
resultado = n1 + (n1*15/100)

print('Seu novo salário é de : {:.2f}'.format(resultado))