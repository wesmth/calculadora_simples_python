while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+ - / *): ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número inteiro!')
    elif operador == '+':
        print('Soma:', int(num_1)+int(num_2))
    elif operador == '-':
        print('Subtração:', int(num_1)-int(num_2))
    elif operador == '/':
        print('Divisão:', int(num_1)/int(num_2))
    elif operador == '*':
        print('Multiplicação:', int(num_1)*int(num_2))
    else:
        print('Operador inválido!')
        