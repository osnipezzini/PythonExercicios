'''
Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''
from emoji import emojize
pt = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
sign = emojize(':arrow_right:', use_aliases=True)
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} {} '.format(pt, sign), end='')
        pt += raz
        cont += 1
    mais = int(input('\nQuantos termos deseja a mais ? Digite 0 para sair'))
print('Progressão finalizada com {} termos.'.format(total))