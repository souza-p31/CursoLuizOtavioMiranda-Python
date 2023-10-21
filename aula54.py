"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os

lista = []
opçoes_validas = 'IAL'

while True:
    print('Selecione uma opção')
    opcao = str(input('[I]nserir [A]pagar [L]istar \n')).upper()[0]
    
    if opcao not in opçoes_validas:
        print('Escolha uma opção válida')
        print()

    if opcao == 'I':
        os.system('cls')
        inserir = str(input('Valor a ser inserido: '))
        lista.append(inserir)
        print(f'O item {inserir} foi inserido.')
        print()
    elif opcao == 'L':
        if len(lista) == 0:
            print('Lista vazia')
            print()
        else:
            print('--- Lista ---')
            for indice,item in enumerate(lista):
                print(indice,item)
            print()
    elif opcao == 'A':
        item_apagar = input('Qual item deseja apagar? ')

        try:
            item_apagar = int(item_apagar)
            item_apagado = lista.pop(item_apagar)
            print(f'O item {item_apagado} foi apagado.')
            print()
        except ValueError:
            print('Insira um número inteiro.')
            print()
        except IndexError:
            print('Não existe um item com esse índice.')
            print()
        except Exception:
            print('Erro desconhecido')
            print()
        
            

