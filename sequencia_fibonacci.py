print('SEQUÊNCIA DE FIBONACCI')
num = int(input('Quantos termos quer exibir da sequência de Fibonacci: '))
t1 = 0
t2 = 1
cont = 3
print(' {} -- {} -- '.format(t1,t2), end=' ')
while cont <= num:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{} -- '.format(t3), end=' ')
    cont += 1
print('FIM')
while True:
    op = str(input('Digite S para sair: ')).strip().upper()
    if op == 'S':
        break
