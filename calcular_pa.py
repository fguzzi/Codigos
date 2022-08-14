print('CALCULAR PA')
while True:
    pri = int(input('Informe o primeiro termo: '))
    raz = int(input('Informe a razão: '))
    qtd = int(input('Informe quantos termos devem ser mostrados: '))
    termo = pri
    i = 1
    while i <= qtd:
        print('{} -- '.format(termo), end=' ')
        termo = termo + raz
        i = i + 1
    print()
    op = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()
    if op == 'N':
        print('ENCERRADO.')
        break
