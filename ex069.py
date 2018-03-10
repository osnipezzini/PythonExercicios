'''
Crie um programa que leia a idade e o sexo de várias pessoas.A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

* - quantas pessoas tem mais de 18 anos
* - quantos homens foram cadastrados
* - quantas mulheres tem menos de 20 anos  
'''

maior = homem = mulher = cont = 0
while True:
    idade = int(input('Digite a idade : '))
    sexo = input("Digite o sexo : M/F").strip().upper()
    cont += 1
    if sexo in 'M':
        homem += 1
    if idade >= 18:
        maior += 1
    if idade <= 20 and sexo in 'F':
        mulher += 1
    opcao = input('Deseja continuar ? S/N').strip().upper()
    if opcao in 'N':
        break
print(f'''
Foram cadastrados {cont} usuários , dentre eles :
{maior} são maiores de idade
{homem} são homens
{mulher} são mulheres e tem menos de 20 anos .''')
