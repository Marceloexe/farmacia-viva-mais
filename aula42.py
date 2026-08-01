frase = 'O python é uuma linguagem de programção ' \
    'Multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.'

i = 0

apareceu_mais_vezes = 0

letra_que_apareceu_mais_vezes = ''

qtd_apareceu_mais_vezes = 0

letra_apareceu_mais_vezes = 0

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_a_letra_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = apareceu_mais_vezes
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print('A letra qe apareceu mais vezes foi '
      f'{letra_apareceu_mais_vezes} que apareceu mais vezes.'
      f'{qtd_apareceu_mais_vezes} x'
)