'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
saida = 0
while saida != 5:
    print('''
    ------ \33[35mSoftware Ellite\33[0;0m -----
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    opcao = int(input('Escolha sua opção: '))
    if opcao == 1:
        print('A soma entre os valores {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('Os valores {} e {} multiplicados é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O valor {} é maior que o valor {}'.format(n1, n2))
        elif n2 > n1:
            print('O valor {} é menor que o valor {}'.format(n1, n2))
        else:
            print('Os valores {} e {} são iguais'.format(n1, n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        exit()
    else:
        print('\33[31mOPÇÃO INVÁLIDA\33[0;0m')