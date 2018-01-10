'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa , calcule seu IMC e mostre seu status de acordo com a tabela abaixo :

-  Abaixo de 18,5: Abaixo do peso
- Entre 18,5 e 25: peso ideal
- 25 até 30; sobrepeso
- 30 até 40: obesidade
- Acima de 40: obesidade mórbida
'''

peso = float(input('Qual seu peso ? '))
altura = float(input('Qual sua altura ? '))

imc = (peso / altura) * altura

if imc < 18.5:
    print('Seu IMC é {} e você está abaixo do peso '.format(imc))
elif imc < 18.5 > 25:
    print('Seu IMC é {} e seu peso é ideal'.format(imc))
elif imc < 25 > 30:
    print('Seu IMC é {} e você tem sobrepeso'.format(imc))
elif imc < 30 > 40:
    print('Seu IMC é {} e você está obeso'.format(imc))
else:
    print('Seu IMC é {} e você tem obesidade mórbida'.format(imc))
