"""
faca uma lista de comprar com listas
o usuario deve ter a possibilidade de
inserir , apagar e listar valores da sua lista
nao permita que o programa quebre com errros
de indices inexistentes na lista.

"""

import os

lista = []

while True:
    print('Selecione uma opçao')
    opcao = input('[i]nserir [a]pagar [l]istar: ')


    if opcao == 'i':
        os.system('clear')
        item = input('item: ')
        ista.append(item)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista [indice]
        except ValueError:
            print('Por favor digite numero inteiro.')
        except IndexError:
            print('Indice nao existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len (lista) == 0:
            print('Nada para listar')

        for i, item in enumerate(lista):
            print(i,item)