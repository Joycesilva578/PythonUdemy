import json

pessoa = {
    'nome': 'Joyce Silva da ',
    'Sobrenome': 'Hora',
    'enderecos': [
        {'rua': 'R1', 'numero': 20},
        {'rua': 'R2', 'numero': 25},
    ],
    'altura': 1.6,
    'numero_preferidos': (5,8,13),
    'dev': True,
    'nada': None
}

with open('aula66.json','w', encoding='utf8') as arquivo:
    json.dump(pessoa,arquivo, ensure_ascii=False,indent=2,)