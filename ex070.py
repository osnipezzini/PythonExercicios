'''
Crie um programa que leia o nome e o preço de vários produtos. o programa deverá perguntar se o usuário vai continuar. No final, mostre:

* Qual é o total gasto na compra
* Quantos produtos custam mais de R$1000
* Qual é o nome do produto mais barato.
'''

caro = barato = precobarato = soma = cont = 0
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$ '))
    opcao = input('Deseja continuar ? S/N').upper().strip()
    if cont == 0 or preco < precobarato:
        barato = nome
        precobarato = preco
    if preco >= 1000:
        caro += 1
    cont += 1
    soma = soma + preco
    if opcao in 'N':
        break
print(f'''
Você cadastrou {cont} produtos , dentre eles :
{caro} produtos custam mais de R$ 1000.00
{barato} é o produto mais barato , custando apenas R$ {precobarato:.2f}
Foram gastos R$ {soma:.2f} nessa compra.''')