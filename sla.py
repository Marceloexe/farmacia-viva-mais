nome = input('Olá, qual o seu nome? ')

print(f'Olá {nome}, gostaria de acessar o sistema?')

print('=====================================')
print('===    Sim, Não ou Com certeza    ===')
print('=====================================')

while True:
    resposta = input('Sua resposta: ').lower()

    if resposta in ['sim', 'com certeza']:
        print('Acessando o sistema...\n')
        print('Sistema aberto')

        
        break

    elif resposta in ['não', 'nao']:
        print('Fechando o sistema...')
        quit()

    else:
        print('Por favor, digite uma das opções válidas')
