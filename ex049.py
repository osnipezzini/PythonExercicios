'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
print()
numero = int(input('Digite um número:'))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(numero, c, numero*c))
