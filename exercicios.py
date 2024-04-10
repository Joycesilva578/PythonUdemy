"""num_inteiro = input('Digite um número inteiro: ')

if num_inteiro.isdigit():
    num_inteiro = int(num_inteiro)

    if num_inteiro % 2 == 0:
        print(f'{num_inteiro} é par')
    else:
        print(f'{num_inteiro} é impar')

else:
    print('isso não é um numero inteiro')
"""
""""
hora = input('digite a hora de 0 a 23: ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('horario deve estar entre 0 ou 23 horas')
    else:
        if hora <= 11:
            print('bom dia')
        elif hora <= 17:
            print('boa tarde')
        else:
            print('boa noite')
else:
    print('digite um horario valido entre 0 a 23 horas')


nome = input('digite seu nome: ')
tamanho = len(nome)
if tamanho <= 4:
    print(f'{nome} tem nome muito curto')

elif tamanho <= 6:
    print(f'{nome} tem nome normal')

else:
    print(f'{nome} tem nome muito grande')
"""

nome = 'Joyce silva da hora'
print(nome.lower()) # tudo minusculo
print(nome.upper()) #tudo maisculo
print(nome.title()) #primeiras letras maisculas

print(nome[-19])