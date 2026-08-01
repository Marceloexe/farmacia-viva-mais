# #nome = input('Qual o seu nome? ')
# #idade = input('Qual a sua idade? ')

# #li_1 = (f'{nome} voce tem {idade}?')
# #resposta = input('sim ou nao? ')

# #if resposta == "sim":
#  #   print('entendi')

# #elif resposta == "nao":
#  #   print ('entao qual a suas verdadeiras informações?')

# #idade_1 = input('')

# primeiro_valor = input('Digite um valor: ')
# segundo_valor = input('Digite um segundo valor: ')

# if primeiro_valor > segundo_valor:
#     print('O primeiro valor é maior que o segundo valor')
    
# elif primeiro_valor == segundo_valor:
#     print('os valores são iguais')

# else:
#     print('O segundo valor é maior que o primeiro valor')

nome = input('Digite seu nome: ').strip()  # Remove espaços extras no início e no fim
idade = input('Digite a sua idade: ')  # Pegamos a idade como string para validar depois

# Verifica se os campos foram preenchidos corretamente
if not nome or not idade.isdigit():  
    print('Desculpa, você deixou campos vazios ou digitou algo inválido!')
else:
    idade = int(idade)  # Converte idade para inteiro apenas se for válida

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if " " in nome:
        print('O seu nome tem espaço')
    else:
        print('O seu nome não tem espaço')

    print(f'O seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')







