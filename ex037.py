'''
Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

def main():
    num = int(input('Digite um numero qualquer : '))

    print('Digite 1 para converter para binário \nDigite 2 para converter para Octal \nDigite 3 para converter para hexadecimal\n')
    escolha = int(input('Selecione uma opção : '))

    if escolha == 1:
        print(bin(num))
    elif escolha == 2:
        print(oct(num))
    elif escolha == 3:
        print(hex(num))
    else:
        print('\033[31m'+'Escolha uma opção válida'+'\033[0;0m')

while True:
    main()
