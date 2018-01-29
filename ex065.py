'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução , mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

key = 'S'
contagem = maior = menor = soma = 0
while key in 'Ss':
    num = int(input('Digite um valor : '))
    if contagem == 0:
        maior = menor = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    contagem += 1
    soma += num
    print('Deseja continuar ? S / N')
    key = input().upper()
media = soma / contagem
print('''
O maior número lido foi {}
O menor número lido foi {}
A soma entre eles é {}
A média entre eles é de {}
'''.format(maior, menor, soma, media))

