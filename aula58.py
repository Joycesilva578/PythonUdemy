# funcoes decoradas

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args,**kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('ok, agora voce foi decorado')
        return resultado
    return interna


def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

inverte_string = criar_funcao(inverte_string)
invertida = inverte_string('123')
print(invertida)