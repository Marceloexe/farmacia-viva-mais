print('Olá, Bem Vindo a farmácia "Viva Mais"')
contador = 0

while True:
    name = input('Qual o seu nome? ')
    resposta_1 = input(f'Oi {name}, temos 4 produtos, gostaria de dar uma olhada? ')

    print('\n')

    produto_one = 'Cylocort'
    produto_two = 'Propionato de clobetasol'
    produto_three = 'Dipirona'
    produto_four = 'Neo Soro'

    preco_one = 27.95
    preco_two = 24.50
    preco_three = 7.50  
    preco_four = 12.00

    desconto_one = preco_one * 0.10

    quantidade_cylo = 0
    quantidade_propi = 0
    quantidade_dip = 0
    quantidade_neo = 0

    if resposta_1.lower() == 'sim':
        while True:
            print(f'1. {produto_one} - R${preco_one:.2f} (com 10% de desconto: R${preco_one - desconto_one:.2f})')
            print(f'2. {produto_two} - R${preco_two:.2f}')
            print(f'3. {produto_three} - R${preco_three:.2f}')
            print(f'4. {produto_four} - R${preco_four:.2f}')

            print('\n')

            try:
             contador =+ 1
             resposta_2 = int(input('Qual das opções gostaria de dar uma olhada (ex: 1 ou 2...) '))
             if resposta_2 not in [1, 2, 3, 4]:
                print('Essa opção não está disponivel, tente novamente')
                continue
            except ValueError:
                print('Por favor, insira uma das opções abaixo.')
                continue

            if resposta_2 == 1:
                print(f'{produto_one}, esse produto está saindo a R${preco_one - desconto_one:.2f}')
                quantidade_cylo += int(input('Quantos você quer? '))

            elif resposta_2 == 2:
                print(f'{produto_two}, esse produto custa R${preco_two:.2f}')
                quantidade_propi += int(input('Quantos você quer? '))

            elif resposta_2 == 3:
                print(f'{produto_three}, esse produto custa R${preco_three:.2f}')
                quantidade_dip += int(input('Quantos você quer? '))

            elif resposta_2 == 4:
                print(f'{produto_four}, esse produto custa R${preco_four:.2f}')
                quantidade_neo += int(input('Quantos você quer? '))

            else:
                print('Essa opção é inválida')

            while True:
                continuar = input('Você gostaria de escolher mais produtos? (sim/não) ').lower()
                if continuar == 'sim':
                    break

                elif continuar in ['não', 'nao']:
                    print('\nSeu pedido até agora:')
                    total_cylo = (preco_one - desconto_one) * quantidade_cylo
                    total_propi = preco_two * quantidade_propi
                    total_dip = preco_three * quantidade_dip
                    total_neo = preco_four * quantidade_neo

                    if quantidade_cylo > 0:
                        print(f'{produto_one}: R${preco_one - desconto_one:.2f} x {quantidade_cylo} = R${total_cylo:.2f}')
                    if quantidade_propi > 0:
                        print(f'{produto_two}: R${preco_two:.2f} x {quantidade_propi} = R${total_propi:.2f}')
                    if quantidade_dip > 0:
                        print(f'{produto_three}: R${preco_three:.2f} x {quantidade_dip} = R${total_dip:.2f}')
                    if quantidade_neo > 0:
                        print(f'{produto_four}: R${preco_four:.2f} x {quantidade_neo} = R${total_neo:.2f}')

                    
                    while True:
                        remover = input('Gostaria de re/mover algum item dessa lista? (sim/não) ').lower()
                        if remover == 'sim':
                            try:
                                opcao_remover = int(input('Digite o número do produto que quer remover: '))
                                if opcao_remover not in [1, 2, 3, 4]:
                                    print('Opção inválida.')
                                    continue

                                if opcao_remover == 1:
                                    qtd_atual = quantidade_cylo
                                elif opcao_remover == 2:
                                    qtd_atual = quantidade_propi
                                elif opcao_remover == 3:
                                    qtd_atual = quantidade_dip
                                else:
                                    qtd_atual = quantidade_neo

                                if qtd_atual == 0:
                                    print('Você não tem unidades desse produto para remover.')
                                    continue

                                qtd_remover = int(input(f'Quantas unidades deseja remover? (máx {qtd_atual}): '))
                                if qtd_remover < 1 or qtd_remover > qtd_atual:
                                    print('Quantidade inválida.')
                                    continue

                                if opcao_remover == 1:
                                    quantidade_cylo -= qtd_remover
                                elif opcao_remover == 2:
                                    quantidade_propi -= qtd_remover
                                elif opcao_remover == 3:
                                    quantidade_dip -= qtd_remover
                                else:
                                    quantidade_neo -= qtd_remover

                                print(f'Removidas {qtd_remover} unidade(s) do produto {opcao_remover}.')

                                print('\nPedido atualizado:')
                                total_cylo = (preco_one - desconto_one) * quantidade_cylo
                                total_propi = preco_two * quantidade_propi
                                total_dip = preco_three * quantidade_dip
                                total_neo = preco_four * quantidade_neo

                                if quantidade_cylo > 0:
                                    print(f'1. {produto_one}: R${preco_one - desconto_one:.2f} x {quantidade_cylo} = R${total_cylo:.2f}')
                                if quantidade_propi > 0:
                                    print(f'2. {produto_two}: R${preco_two:.2f} x {quantidade_propi} = R${total_propi:.2f}')
                                if quantidade_dip > 0:
                                    print(f'3. {produto_three}: R${preco_three:.2f} x {quantidade_dip} = R${total_dip:.2f}')
                                if quantidade_neo > 0:
                                    print(f'4. {produto_four}: R${preco_four:.2f} x {quantidade_neo} = R${total_neo:.2f}')

                            except ValueError:
                                print('Por favor, insira um número válido.')

                        elif remover in ['não', 'nao']:
                           break
                
                else:
                    print('Por favor digite sim ou não')

                break

            if continuar != 'sim':
                break

        break

    elif resposta_1.lower() == 'não' or resposta_1.lower() == 'nao':
        print('Tudo bem, volte sempre')
        quit()

    else:
        print('Não estou entendendo a sua resposta, tente novamente')

total_cylo = (preco_one - desconto_one) * quantidade_cylo
total_propi = preco_two * quantidade_propi
total_dip = preco_three * quantidade_dip
total_neo = preco_four * quantidade_neo

total_a_pagar = total_cylo + total_propi + total_dip + total_neo

print('\n======== Cupom Fiscal ========')
print(f'Cliente: {name}')

if quantidade_cylo > 0:
    print(f'{produto_one}: R${preco_one - desconto_one:.2f} x {quantidade_cylo} = R${total_cylo:.2f}')
if quantidade_propi > 0:
    print(f'{produto_two}: R${preco_two:.2f} x {quantidade_propi} = R${total_propi:.2f}')
if quantidade_dip > 0:
    print(f'{produto_three}: R${preco_three:.2f} x {quantidade_dip} = R${total_dip:.2f}')
if quantidade_neo > 0:
    print(f'{produto_four}: R${preco_four:.2f} x {quantidade_neo} = R${total_neo:.2f}')

print('\n======== Total A Pagar ========')
print(f'Total: R${total_a_pagar:.2f}')

print(contador)

