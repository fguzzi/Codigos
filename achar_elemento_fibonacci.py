print('ENCONTRAR TERMO NA SEQUENCIA FIBONACCI')
while True:
    n = int(input("Que termo deseja encontrar: "))
    ultimo=1
    penultimo=1
    if (n==1) or (n==2):
        print(f' O {n}º termo é 1')
    else:
        for count in range(2,n):
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
        print(f' O {n}º termo é {termo}')
    op = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()[0]
    if op == 'N':
        print('Encerrado.')
        break
