palavra_secreta = 'banana'
letras_acertadas = ''

while True:
    entrada = input('Digite uma letra: ')

    if len(entrada) > 1:
        print('Digite apenas uma letra')
        continue

    if entrada in palavra_secreta:
        letras_acertadas += entrada 

    print(f'Letras acertadas: {letras_acertadas} ')

    palavra_forrmada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_forrmada += letra_secreta

        else:
            palavra_forrmada += '*'

    print(palavra_forrmada)
