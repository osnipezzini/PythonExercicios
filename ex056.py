'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.No final do programa, mostre:
* A média de idade do grupo.
* Qual é o nome do homem mais velho.
* Quantas mulheres tem menos de 20 anos.
'''
velho = 0
menor = 0
somaidade = 0
maiorhomem = 0
for pessoa in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoa))
    nome = str(input('Digite o nome : ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo : \n( M ) Masculino ( F ) Feminino > ')).strip()
    somaidade += idade
    if pessoa == 1:
        velho = nome
        maiorhomem = idade
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        velho = nome
    if idade < 20 and sexo in 'Ff':
        menor += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(int(mediaidade)))
print('O homem mais velho é {} e tem {} anos '.format(velho, maiorhomem))
print('{} mulheres tem menos de 20 anos '.format(menor))
