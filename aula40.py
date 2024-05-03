Perguntas = [
    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opcoes': ['1', '3', '4', '5'],
        'Respostas': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55','10', '51'],
        'Respostas': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Respostas': '5',
    },
]

qtd_acertos = 0
for Pergunta in Perguntas:
    print('Pergunta:', Pergunta['Pergunta'])
    print()

    for i, opcao in enumerate(Pergunta['Opcoes']):
        print(f'{chr(ord("a") + i)})', opcao)
    print()

    escolha = input('Escolha uma opcao: ').lower()
    print()

    acertou = False

    if escolha in ['a', 'b', 'c', 'd']:
        if Pergunta['Opcoes'][ord(escolha) - ord('a')] == Pergunta['Respostas']:
            acertou = True


    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')

print('Voce acertou', qtd_acertos, 'Perguntas')
