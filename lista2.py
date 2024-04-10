secreto = 'bicicleta'
digitados = []

while True:
    letra = input('Digite uma letra de A a Z: ')

    if len (letra) > 1:
        print('Digite uma letra valida de A a Z.')
        continue

    digitados.append (letra)

    if letra in secreto:
        print(f'Eba, voce digitou uma letra que contem na palavra secreta.')
    else:
        print(f'Erro, voce digitou uma letra que não contém na palavra secreta')
        digitados.pop()


        secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

        print(secreto_temporario)