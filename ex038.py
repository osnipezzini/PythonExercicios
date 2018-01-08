'''
Escreva um programa que leia dois numeros inteiros e compare-os , mostrando na tela uma mensagem :
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior , os dois são iguais 
'''

num1 = int(input('Digite o primeiro numero '))
num2 = int(input('Digite o segundo numero'))

if num1 < num2:
    print('O primeiro numero é menor que o segundo numero')
elif num1 > num2:
    print('O primeiro numero é maior que o segundo numero')
elif num1 == num2:
    print('Os dois numeros são iguais')