print('FATORIAL')
num = int(input('Insira um nº para saber seu fatorial: '))
fatorial = 1
if num < 0:
   print('Não existe fatorial de número negativo')
elif num == 0:
   print('O fatorial de 0 é igual a 1')
else:
    for c in range(1, num + 1):
        fatorial = fatorial * c
    print('{} ! é igual a {} '.format(num, fatorial))
while True:
    op = str(input('Digite S para sair: ')).strip().upper()
    if op == 'S':
        break
