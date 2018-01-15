'''
Crie um programa que faça o computador jogar Jokenpô com você
'''
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é sua jogada ? '))
print('-='*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
if computador == 0: # Computador jogou pedra
	if jogador == 0:
		print('EMPATOU')
	elif jogador == 1:
		print('VOCÊ GANHOU')
	elif jogador == 2:
		print('VOCÊ PERDEU')
	else:
		print('JOGADA INVÁLIDA')
elif computador == 1: # Computador jogou papel
	if jogador == 0:
		print('VOCÊ PERDEU')
	elif jogador == 1:
		print('EMPATOU')
	elif jogador == 2:
		print('VOCÊ GANHOU')
	else:
		print('JOGADA INVÁLIDA')
elif computador == 2: # Computador jogou tesoura
	if jogador == 0:
		print('VOCÊ GANHOU')
	elif jogador == 1:
		print('VOCÊ PERDEU')
	elif jogador == 2:
		print('EMPATOU')
	else:
		print('JOGADA INVÁLIDA')
print('-='*20)