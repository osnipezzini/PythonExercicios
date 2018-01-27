'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 
'''
num = int(input('Digite um número: '))
raz = num + 1
tot = 0
for c in range(1, raz):
    if num % c == 0:
        print('\033[34m {}'.format(c), end='')
        tot += 1
    else:
        print('\033[31m {}'.format(c), end='')
print('\n\033[mO número {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')