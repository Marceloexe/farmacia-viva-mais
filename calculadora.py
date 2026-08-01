# Calculadora com While

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*): ')

    numeros_validos = None

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando a sua conta abaixo: ')

    if operador == '+':
        print(numero_1 + numero_2)

    elif operador == '-':
        print(numero_1 - numero_2)

    elif operador == '*':
        print(numero_1 * numero_2)

    else:
        print(numero_1 / numero_2)
    

    sair = input('Você deseja sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break