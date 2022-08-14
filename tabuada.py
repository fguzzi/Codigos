print('TABUADA')
n = t = cont = l = 0
while True:
    n = int(input('Quer ver a tabuada de que nº: '))
    if n < 0:
        break
    l = int(input('Digite a quantidade de multiplicações: '))
    print('-' * 55)
    for cont in range(1, l + 1):
        t = cont * n
        print('{} x {} = {}'.format(n, cont, t))
        cont += 1
    print('-' * 55)
    op = str(input('Deseja ver outra tabuada? [ S/N ]: ')).strip().upper()
    if op == 'N':
        print('Programa de tabuada encerrado. Volte sempre !!')
        break
        