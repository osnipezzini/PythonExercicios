'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Digite seu sexo : M/F')).upper().strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('\033[31mDados inválido , tente novamente! ')).upper().strip()[0]
print('\033[34mSexo {} registrado com sucesso'.format(sexo))