#atributos de classe exercicio
import json

CAMINHO_ARQUIVO = 'Aula73.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Joao',33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('fazendo dump')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

