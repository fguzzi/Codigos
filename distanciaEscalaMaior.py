print('----DISTÂNCIAS ENTRE NOTAS PARTINDO DA TÔNICA----')
print('--------------------------ESCALA  MAIOR---------------------------------')
notas = ['Primeira', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sétima', 'Oitava']
dist = [1,2,2.5, 3.5, 4.5, 5.5, 6]
while True:
    print('''Qual a posição da nota na escala?
               [ 2 ] - Segunda
               [ 3 ] - Terça
               [ 4 ] - Quarta
               [ 5 ] - Quinta
               [ 6 ] - Sexta
               [ 7 ] - Sétima
               [ 8 ] - Oitava''')
    esc = int(input('Digite: '))
    print(f' Você escolheu {notas[esc-1]}')
    if esc == 1:
        print(f' Não há distância.')
    else:
        print(f' A distância é de {dist[esc-2]} tom(s)')
    op = str(input('Deseja continuar? [ S/N ]: ')).strip().upper()[0]
    if op == 'N':
        break
print('Programa encerrado.')
