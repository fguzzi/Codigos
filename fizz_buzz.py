print('FIZZBUZZ')
print('Se for múltiplo de 3 = Fizz.')
print('Se for múltiplo de 5 = Buzz.')
print('Se for múltiplo de 3 e 5 ao mesmo tempo = FizzBuzz.')
print('Se não for múltiplo nem de 3 nem de 5 = não.')
while True:
    num = int(input('Digite um número inteiro: '))
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print('Não.')
    op = str(input('Deseja continuar? [ S/N ]: ')).strip().lower()
    if op == 'n':
        print('ENCERRADO.')
        break
