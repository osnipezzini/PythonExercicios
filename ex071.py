'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado ( numero inteiro ) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$20, R$10 e R$1
'''

cinquenta = vinte = dez = um = 0
sacar = int(input('Quanto quer sacar ?'))
while sacar >= 50:
    sacar -= 50
    cinquenta += 1
while sacar >= 20:
    sacar -= 20
    vinte += 1
while sacar >= 10:
    sacar -= 10
    dez += 1
while sacar >= 1:
    um += 1
    sacar -= 1
print(f'''
Vou lhe entregar {cinquenta} notas de R$ 50,00 , {vinte} notas de R$ 20,00 , {dez} notas de R$10,00 e {um} notas de R$ 1,00''')