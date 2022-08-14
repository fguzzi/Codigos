print('CONVERSOR DE MEDIDAS')
while True:
    print(''' Opções de conversão:
    [ 1 ] - Nós em Km/h
    [ 2 ] - Milhas em km
    [ 3 ] - Jardas em m''')
    op = int(input('Digite sua opção: '))
    if op == 1:
        ns = float(input('Digite nós: '))
        km = ns * 1.852
        print('{:.2f} Kt equivalem a {:.2f} Km/h'.format(ns, km))
    elif op == 2:
        ml = float(input('Digite milhas: '))
        km = ml * 1.852
        print('{:.2f} NM equivalem a {:.2f} Km'.format(ml, km))
    elif op == 3:
        jd = float(input('Digite jardas: '))
        m = jd * 0.9144
        print('{:.2f} yd equivalem a {:.2f} m'.format(jd, m))
    else:
        print('Opção Inválida. Tente novamente.')
    op = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()
    if op == 'N':
        break
print('Encerrado.')
