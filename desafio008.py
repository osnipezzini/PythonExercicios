# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Digite um valor : '))

print('A conversão em centímetros de {} é {:.2f}'.format(n1, n1*100))
print('A conversão em milímetros de {} é {:.2f}'.format(n1, n1*1000))
