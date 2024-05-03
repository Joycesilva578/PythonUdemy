"""
Exercicios com funcoes

criei uma funcao que multiplica todos os argumentos
nao nomeados recebidos
retorne o total o total para uma variavel e mostr o valor
da variavel

crie uma funcao fala se um numero é par ou impar
e retorne se o numero é par ou impar
"""

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)

#####################################################

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(3))