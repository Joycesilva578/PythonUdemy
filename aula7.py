entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada  == 'E' and entrada == 'e') or senha_digitada == senha_permitida:
    print('voce entrou no sistema')

else:
    print('voce nao entrou no sistema')

