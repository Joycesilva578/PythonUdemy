"""
list comprehension python
"""

import pprint

def p (v):
    pprint.pprint(v,sort_dicts=False, width=40)

lista = [
    numero * 2
    for numero in range(10)
]

##print(list(range(10)))
##print(lista)

#Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep='\n')
p(novos_produtos)