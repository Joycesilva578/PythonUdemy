"""
while True: #loop infinito
    nome = input("qual seu nome: ")
    print(f"Ola seu nome é {nome}")

x = 0
while x < 10:
    if x == 9:
        x = x + 1
        break
    print(x)
    x = x + 1
print('acabou')

----------------------------------------------------------------------------------------------------------
while True:
    print()
    num_1 = input('digite um numero: ')
    num_2 = input('digite outro numero: ')
    operador = input('digite um operador matematico: ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('voce precisa digitar um numero')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('operador não reconhecido')

    sair = input('deseja sair da calculadora: [s]im ou [n]ão:')
    if sair == 's':
        break

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador +=1

else:
    print ('cheguei no else')
"""

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1
