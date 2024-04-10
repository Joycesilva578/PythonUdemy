nome = input('qual seu nome: ')
idade = input ('qual sua idade : ')

idade = int(idade)

idade_limite = 18

if idade >= idade_limite:
   print (f'{nome} pode pegar emprestimo')
else:
    print(f'{nome} não pode pegar emprestimo')