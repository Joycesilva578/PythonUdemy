# groupby agrupar valores

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Joyce','nota': 'B'},
    {'nome': 'Noah','nota': 'B'},
    {'nome': 'Julia', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Luiza', 'nota': 'C'},
    {'nome': 'Joao', 'nota': 'A'},
    {'nome': 'Lucas', 'nota': 'D'}
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos,key=ordena)
grupos = groupby(alunos_agrupados,key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)


