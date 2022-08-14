print('='*30)
print('             PALPITES PARA MEGA SENA                     ')
print('='*30)
from time import sleep
from random import randint
from time import sleep
cont = 0
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer fazer?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('==' * 3, f' SORTEANDO {quant} JOGO(S)', '==' * 3,)
for i, l in enumerate(jogos):
    print(f' Jogo {i+1} : {l}')
    sleep(2)
while True:
    op = str(input('Digite S para sair: ')).strip().upper()
    if op == 'S':
        print("Encerrado. Boa sorte.")
        break
