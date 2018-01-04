'''
Crie um programa que leia duas notas de um aluno e calcule sua média , mostrando uma mensagem no final , de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior : APROVADO
'''

num1 = float(input("Digite sua primeira nota: " ))
num2 = float(input("Digite sua segunda nota: "))

media = (num1 + num2) / 2

if media < 5.0:
    print('Você foi reprovado! ')
elif media >= 7.0:
    print('Você foi aprovado. ')
else:
    print('Você está em recuperação')