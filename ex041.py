'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria , de acordo com sua idade :

- Até 9 anos: Mirim
- Até 14 anos : Infantil
- Até 19 anos : Junior
- Até 20 anos : Senior
- Acima : Master
'''

ano = int(input('Qual o seu ano de nascimento: '))

idade = 2018 - ano

if idade <= 9:
    print('Você tem {} e sua classificação atual é Mirim'.format(idade))
elif idade <= 14:
    print('Você tem {} e sua classificação atual é Infantil'.format(idade))
elif idade <= 19:
    print('Você tem {} e sua classificação atual é Junior'.format(idade))
elif idade == 20:
    print('Você tem {} e sua classificação atual é Senior'.format(idade))
else:
    print('Você tem {} e sua classificação atual é Master'.format(idade))
