#Escreva um programa que pergunte a quantidade de Km percorridos por um carro e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar , sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km = float(input('Qual a quantidade de Km rodados ? '))
dias = int(input('Por quantos dias ele foi alugado ? '))
pago = (dias * 60) + (km * 0.15)
print('Você rodou {}Km e alugou por {} dias e irá pagar R${:.2f}'.format(km, dias, pago))