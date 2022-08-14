print('ANALISAR NÚMERO PRIMO')
while True:
    num = int(input('Digite um número para descobrir se é primo: '))
    tot = 0
    for c in range(1,num + 1):
        if num % c == 0:
            tot = tot + 1
    if tot == 1 or tot > 2:
        print(f' O número {num} não é primo.')
    if tot == 2:
        print(f'O número {num} é primo.')
    op = str(input('Quer contiunar? [ S/N ]: ')).strip().upper()
    if op == 'N':
        print('Encerrado.')
        break
