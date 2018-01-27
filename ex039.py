import datetime
from time import sleep

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
def homem():
    if idade < 18:
        print('Ainda não está na hora de se alistar, faltam {} ano(s) para se alistar'.format(18 - idade))
    elif idade == 18:
        print('Já está na hora de se alistar')
    elif idade > 18:
        print('Passou {} ano(s) do tempo de se alistar'.format(idade - 18))
def sex():
    sexo = str(input('Você é homem ou mulher ?\nDigite H para homem e M para mulher')).upper()
    mensagem = 'Você nasceu em {} e tem {} anos'.format(nasc, idade)
    if sexo == 'M':
        print(mensagem + ', mas como você é mulher não precisa se alistar')
    elif sexo == 'H':
        print(mensagem)
        homem()
    else:
        print('Digite um sexo válido')
        sleep(1)
sex()