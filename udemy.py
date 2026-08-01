# entrada_1 = int(input('Digite um número inteiro: '))
# print(entrada_1)

# if entrada_1 % 2 == 0:
#     print('Este número é par')

# else:
#     print('Este número é ímpar')

# entrada_2 = int(input('Qual é a hora de agora?:(ex: 13 14 15) '))
# bom_dia = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# boa_tarde = (13, 14, 15, 16, 17)
# boa_noite = (18, 19, 20, 21, 22, 23)

# if entrada_2 in bom_dia:
#     print('Bom dia')

# elif entrada_2 in boa_tarde:
#     print('Boa tardee')

# elif entrada_2 in boa_noite:
#     print('Boa noite')

# else:
#     print('Algo inválido')

# entrada_3 = str(input('Digite seu primeiro nome: '))
# nome = len(entrada_3)

# if nome <= 4:
#     print('O seu nome é pequeno')

# elif nome == 5 or nome == 6:
#     print('O seu nome tem o tamanho normal')

# elif nome > 6:
#     print('Seu nome é grande')

# else:
#     print('Você nao digitou seu nome!!')

# entrada = int(input('Digiete um número inteiro: '))

# print(entrada)

# while entrada:
#     print(f'O número inteiro que você digitou é {entrada}')

#     break

# contador = 0

# while contador <= 100:
#     contador += 1

#     if contador == 4:
#         print('Não vou mostrar o 4.')
#         continue

#     if contador >= 10 and contador <= 27:
#         print(f'Não vou mostrar o {contador}')
#         continue

#     print(contador)

#     if contador == 99:
#         break

# print('Acabou')

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}-{coluna=}')
        coluna += 1
    linha += 1

print('Acabou')