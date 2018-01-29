'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final , mostre quantos números foram digitados e qual foi a soma entre eles ( desconsiderando o flag).
'''
key = soma = contagem = 0
while key != 999:
    key = int(input('Digite um valor: '))
    if key != 999:
        soma += key
        contagem += 1
print('Foram digitados {} números e a soma entre eles é {}'.format(contagem, soma))