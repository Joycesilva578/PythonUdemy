senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'sua senha({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
