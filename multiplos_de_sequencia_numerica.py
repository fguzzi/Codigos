print('MÚLTIPLOS EM UMA SEQUENCIA NUMÉRICA')
while True:
        i = int(input('Digite o número inicial da sequência: '))
        f = int(input('Digite o número final da sequência: '))
        if i >= f:
            print('O número inicial é maior que o final. Tente novamente.')
            break
        m = int(input('Quer achar os múltiplos de qual número: '))
        c = 0
        print('=' * 30)
        print(f' Múltiplos de {m} na sequência de {i} a {f} são:  ')
        for cont in range(i, f + 1):
            if cont % m == 0:
                c += 1
                print(cont, end=' ')
                print()
        print(f' Total de {c} números.')
        print('=' * 30)
        op = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()
        if op == 'N':
            break




