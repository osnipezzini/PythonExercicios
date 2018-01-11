'''
Elabore um programa que calcule o valor a ser pago por um produto , considerando o seu preço normal e condição de pagamento:

- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão : 5% de desconto
- em até 2x no cartão : preço normal
- 3x ou mais no cartão: 20% de juros
'''

preco = float(input('Qual o valor do produto ? '))
print('Digite 1 para pagamento em dinheiro. \nDigite 2 para pagar no cartão.')
escolha = int(input('Digite a opção desejada ! '))


if escolha == 1:
    preconovo = preco - (preco * 10 / 100)
    print('O valor a ser pago é de {}'.format(preconovo))
elif escolha == 2:
    vezes = int(input('Em quantas vezes deseja parcelar ? '))
    if vezes == 1:
        preconovo = preco - (preco * 5 / 100)
        print('O valor a ser pago é de {} '.format(preconovo))
    elif vezes == 2:
        print('O preço a ser pago é de {} dividido em {} vezes '.format(preco, vezes))
    else:
        preconovo = preco + (preco * 20 / 100)
        print('O valor a ser pago é de {} , dividido em {} vezes'.format(preconovo, vezes))
else:
    print('Digite uma opção válida!')
