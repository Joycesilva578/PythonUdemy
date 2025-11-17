#recursiva

def recursiva(inicio=0, fim=10):
    #caso base
    if inicio >= fim:
        return fim

    #caso recursivo
    #contas ate chegar ao final

    inicio += 1
    return recursiva(inicio,fim)

print(recursiva())