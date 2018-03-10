'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
cont = 0
while True:
    cpu = randint(0, 10)
    pc = int(input('Digite um número: '))
    opcao = input('Par ou Impar ? P/I').upper().strip()
    soma = pc + cpu
    par = soma % 2 == 0
    impar = soma % 2 == 1
    print(f'Você escolheu {pc} e o computador escolheu {cpu} e o resultado foi : {soma}')
    if par and opcao in 'P':
        print('Você ganhou! ')
        cont += 1
    elif impar and opcao in 'I':
        print('Você ganhou!')
        cont += 1
    else:
        break
if cont == 0:
    print('Você não conseguiu nenhuma vitória !')
elif cont == 1:
    print('Você obteve apenas uma vitória . Tente novamente !')
else:
    print(f'Você obteve {cont} vitórias consecutivas . Parabéns !!')