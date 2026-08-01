var = 'qualquer|valor'

i = 0
while i < len(var):
    palavra = var[i]

    if ' ' in palavra:
        break


    print(palavra)
    i += 1

else:
    print('Nào encontrei um espaço na string.')

print('Fora do while.')