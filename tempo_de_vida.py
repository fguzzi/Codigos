print('CALCULO IDADE')
idade = int(input('Digite sua idade: '))
ttmeses = idade * 12
ttdias = idade * 365
tthoras = ttdias * 24
ttminutos = tthoras * 60
ttsegundos = ttminutos * 60
print(f'{idade} anos correspondem a: \n{ttmeses} meses,\n{ttdias:,} dias,\n{tthoras:,} horas,\n{ttminutos:,} minutos, \n{ttsegundos:,} segundos.')
while True:
    op = str(input('Digite S para sair: ')).strip().upper()
    if op == 'S':
        break
