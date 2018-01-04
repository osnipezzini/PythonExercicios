import datetime


'''
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade :

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

nasc = int(input('Em que ano você nasceu ? '))

now = datetime.datetime.now()

idade = now.year - nasc

if idade < 18:
    print('Ainda não está na hora de se alistar, faltam {} para se alistar '.format(18 - idade))
elif idade == 18:
    print('Já está na hora de se alistar')
else:
    print('Passou {} ano(s) do tempo de se alistar '.format(idade - 18))