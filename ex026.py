#Faça um programa que leia uma frase pelo teclado e mostre:
#- Quantas vezes aparece a letra 'A'" \
#- Em que posição ela aparece a primeira vez" \
#- Em que posição ela aparece a ultima vez"
from format import style

entra = str(input('Digite uma frase: ')).upper().strip()
style()
print('A letra A aparece {} vezes na frase.'.format(entra.count('A')))
print('A primeira letra A apareceu na posição {}'.format(entra.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(entra.rfind('A')+1))
style()