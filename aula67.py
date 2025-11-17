def adiciona_cliente(nome,Lista=None):
    if Lista is None:
        Lista=[]
    Lista.append(nome)
    return Lista

cliente1 = adiciona_cliente('Joyce')
adiciona_cliente('Matheus', cliente1)
adiciona_cliente('Pedro', cliente1)
cliente1.append('Luiz')
print(cliente1)

