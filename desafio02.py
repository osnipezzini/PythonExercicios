from datetime import datetime

dia = input('Qual dia você nasceu ? ')
mes = input('Qual mês você nasceu ? ')
ano = input('Qual ano você nasceu ? ')

anoAtual = datetime.now().year
anoInt = int(ano)
idadeAtual = anoAtual - anoInt
idadeStr = str(idadeAtual)
print('Você nasceu no dia ' + dia + ' de ' + mes + ' de ' + ano + '\nVocê tem atualmente ' + idadeStr + ' anos')
