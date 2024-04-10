""""
interavel -- str,range
iterador - quem sabe entregar um valor por vez
next -- entrega prox numero
iter -- me entrega o seu iterador

como FOR  funciona por baixo dos panos
"""

texto = 'joyce'
iteratador = iter(texto)


while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)