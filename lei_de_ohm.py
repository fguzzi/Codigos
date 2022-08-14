print('LEI DE OHM - CALCULOS')
while True:
    print(''' O que deseja calcular? 
                    - Corrente [ I ] 
                    - Tensão [ V ]
                    - Resistência [ R ] ''')
    op = str(input('Digite sua escolha: ')).strip().upper()[0]
    if op == 'R':
        v = float(input('Digite o valor da Tensão (em Volts): '))
        i = float(input('Digite o valor da Corrente (em Amperes): '))
        r = v / i
        print(f' O valor da Resistência = {r:.1f} Ohms.')
    elif op == 'V':
        i = float(input('Digite o valor da Corrente (em Amperes): '))
        r = float(input('Digite o valor da Resistância (em Ohms): '))
        v = r * i
        print(f' O valor da Tensão = {v:.1f} Volts.')
    elif op == 'I':
        v = float(input('Digite o valor da Tensão (em Volts): '))
        r = float(input('Digite o valor da Resistância (em Ohms): '))
        i = v / r
        print(f' O valor da Corrente = {i:.2f} Amperes.')
    else:
        print('Opção inválida !!! Tente novamente.')
    esc = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()[0]
    if esc == 'N':
        print('Encerrado')
        break

