print('CONVERSOR DE DECIMAL PARA OCTAL E HEXADECIMAL')
while True:
    num = int(input('Digite um número inteiro: '))
    print('Escolha uma das bases para conversão: ')
    print('[ 1 ] converter para BINÁRIO: ')
    print('[ 2 ] converter para OCTAL: ')
    print('[ 3 ] converter para HEXADECIMAL: ')
    opção = int(input('Sua opção: '))
    if opção == 1:
        print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
    elif opção == 2:
        print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
    elif opção == 3:
        print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
    else:
        print('Opção inválida. Tente novamente.')
    esc = str(input('Deseja continuar? [ S/N ]: ')).strip().lower()
    if esc == 'n':
        print('ENCERRADO,')
        break
