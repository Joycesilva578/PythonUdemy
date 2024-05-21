def executa(funcao, *args):
    return funcao(*args)

duplica = executa(
    lambda m: lambda n:n * m,
    3
)

print(duplica(2))

print(
    executa(
        lambda x,y: x + y,
        2,3
    ),
)