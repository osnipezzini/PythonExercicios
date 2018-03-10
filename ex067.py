'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

tabuada = cont = 0
while True:
    cont = 0
    numero = int(input('Digite um número que lhe mostrarei a tabuada: '))
    if numero < 0:
        print('Número negativos não são aceitos ! ')
        break
    while cont <= 10:
        tabuada = numero * cont
        print(f'{numero} X {cont} = {tabuada}')
        cont += 1