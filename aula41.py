#exercicios usando sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Parabens voce digitou letra l')
        break

    print(letras)