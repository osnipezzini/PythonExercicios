'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado ( numero inteiro ) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$20, R$10 e R$1
'''
print('=' * 30)
print('{:^30}'.format('BANCO ELLITE'))
print('=' * 30)
cinquenta = vinte = dez = um = 0
sacar = int(input('Quanto quer sacar ?'))
while True:
    if sacar >= 50:
        sacar -= 50
        cinquenta += 1
    elif sacar >= 20:
        sacar -= 20
        vinte += 1
    elif sacar >= 10:
        sacar -= 10
        dez += 1
    elif sacar >= 1:
        um += 1
        sacar -= 1
    else:
        break

if cinquenta != 0:
    print(f'{cinquenta} cédulas de R$50.00')
if vinte != 0:
    print(f'{vinte} cédulas de R$20.00')
if dez != 0:
    print(f'{dez} cédulas de R$10.00')
if um != 0:
    print(f'{um} cédulas de R$1.00')