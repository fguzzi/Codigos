print("--------JOGO DE ADVINHAÇÃO--------")
from random import randint
print('EU PENSEI EM UM NUMERO DE 1 A 20.')
print('VOCÊ TERÁ 3 TENTATIVAS PARA ADVINHAR.')
while True:
    sorteio = randint(1, 20)
    palpite = 0
    tentativas = 0
    while True:
        palpite = int(input('SEU PALPITE: '))
        if sorteio > palpite:
            print('O número é MAIOR !')
            tentativas += 1
        elif sorteio < palpite:
            print('O número é MENOR !')
            tentativas += 1
        else:
            print(f' EU ESCOLHI {sorteio} ! PARABÉNS, VOCÊ ADVINHOU !!!')
            break
        if tentativas == 3:
            print(f'VOCÊ ESGOTOU 3 TENTATIVAS! O NÚMERO ERA {sorteio}')
            break
    op = str(input('DESEJA JOGAR NOVAMENTE? [ S/N ]: ')).strip().upper()
    if op == 'N':
        print('ATÉ LOGO !!')
        break
