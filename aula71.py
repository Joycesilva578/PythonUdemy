#escopo da classe e do metodo da classe

class Animal:

    def __init__(self,nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self,alimento):
        return f'{self.nome} está comendo a {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal(nome='Leao')
print(leao.nome)
print(leao.executar('maça'))