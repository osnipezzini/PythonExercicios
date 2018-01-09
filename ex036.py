'''Escreva um programa para aprovar o empréstimo para a compra de uma casa. O programa vai perguntar o valor da casa , o salario do comprador e em quantos anos ele vai pagar:

 Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%¨do salário ou então emprestimo será negado.
'''

valor = float(input('Digite o valor da casa : '))
salario = float(input('Digite seu sálário : '))
parcela = int(input('Em quantas vezes quer pagar ? '))
#perce = salario
presta = valor / parcela

if ((salario * 30) / 100) < parcela:
    print('\033[31m'+'Empréstimo negado')
else:
    print('O valor da prestação mensal é de {:.2f}'.format(presta))