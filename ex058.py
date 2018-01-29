'''
Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
cpu = randint(0, 10)
pc = 99
tentativas = 1
print(cpu)
while cpu != pc:
    pc = int(input('Adivinhe o que pensei : '))
    if cpu < pc:
        print('Menos , tente novamente !!')
    if cpu > pc:
        print('Mais , tente novamente !')
    if pc != cpu:
        tentativas += 1
    if tentativas == 1 and pc == cpu:
            print('PARABÉNS VOCÊ ACERTOU DE PRIMEIRA! ')
    if pc == cpu and tentativas != 1:
        print('\033[32mACERTOU\033[0;0m , você utilizou {} tentativas.'.format(tentativas))