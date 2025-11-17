class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Joyce', 'Hora') ##criando um novo objeto
#p1.nome = 'Joyce'
#p1.sobrenome = 'Hora'

p2 = Pessoa('Joyce', 'Silva')
#p2.nome = 'Joyce'
#p2.sobrenome = 'Silva'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
