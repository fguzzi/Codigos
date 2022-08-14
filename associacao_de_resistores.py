print('ASSOCIAÇÃO DE RESISTORES')
while True:
    soma = pr = req = 0
    t = str(input('Associação em série ou paralelo [ S/P ]: ')).strip().lower()[0]
    q = int(input('Quantos resistores você quer associar?: '))
    for c in range(0, q):
        r = float(input(f' Digite o {c + 1}º resistor em Ohms: '))
        if t == 'p':
            pr = 1 / r
            soma = soma + pr
            req = (1 / soma)
        if t == 's':
            req = req + r
    print(f' A resistência equivalente é {req:.2f} Ohms.')
    op = str(input('Deseja continuar? [ S/N ]: ')).strip().lower()[0]
    if op == 'n':
        print('ENCERRADO.')
        break
