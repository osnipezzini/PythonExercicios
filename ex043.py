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

imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ')
elif 18.5 <= imc < 25:
    print('Seu peso é ideal')
elif 25 <= imc < 30:
    print('Você tem sobrepeso')
elif 30 <= imc < 40:
    print('Você está obeso')
else:
    print('Obesidade mórbida')
