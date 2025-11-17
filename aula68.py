import json
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas,tarefas_refazer):
    print()
    if not tarefas:
        print('nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()

def refazer(tarefas,tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adiciona na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('voce nao digitou uma tarefa')
        return
    print(f'{tarefa=} adicionada na lista')
    tarefas.append(tarefa)
    print()

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo nao existe')
        salvar(tarefas,caminho_arquivo)
    return dados

def salvar (tarefas,caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo,'w', encoding='utf-8') as arquivo:
        dados = json.dump(tarefas,arquivo,indent=2,ensure_ascii=False)
        return dados

caminho_arquivo = 'aula68.json'
tarefas = ler ([], caminho_arquivo)
tarefas_refazer = []

while True:
    print('Comando: listar, desfazer e refazer')
    tarefa = input('digite uma tarefa ou comando:')
    salvar(tarefas, caminho_arquivo)

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas,tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa,tarefas)
        listar(tarefas)
        continue
