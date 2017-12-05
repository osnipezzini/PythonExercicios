while True:
    n = float(input('Digite sua nota: '))
    if n.isdigit():
        continue
    else:
        print('São aceitos apenas valores numéricos !')
    if n == "":

