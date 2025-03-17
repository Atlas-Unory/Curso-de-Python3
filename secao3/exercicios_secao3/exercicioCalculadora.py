#calculadora com while

while True:
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite um operador (+-*/): ')

    numero_validos = None
    try:
        num_1_float = 0
        num_2_float = 0

        numero_validos = True
    except:
        numero_validos = None

    if numero_validos is None:
        print('um ou ambos os numeros digitados são invalidos')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue


    print('Realizando sua conta, confira o resultado abaixo:')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break