"""
Empacotamento e desempacotamento de dicionarios
*args refere-se a argumento nao nomeados
kwargs refere-se a argumentos nomeados vao ser empacotados na funcao, utilizando 2 *
"""

a,b = 1,2
a,b = a,b
print(a,b)

pessoa = {
    'nome': 'Joyce',
    'sobrenome': 'Hora',
}

""" (a1,a2),(b1,b2) = pessoa.items()
print(a1,a2)
print(b1,b2)"""

dados_pessoa = {
    'idade': 24,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

def mostra_argumentos_nomeados(*args, **kwargs):
    for chave,valor in kwargs.items():
        print(chave,valor)

mostra_argumentos_nomeados(nome='Joyce',qlq=123)