"""
isistance - para saber se o objeto é de determinado tipo

"""

lista = ['a', 1, 1.1, True, [0,1,2], (1,2),
         {0,1}, {'nomw': 'Joyce'},
]
for item in lista:
    if isinstance(item,set):
        print('Set')
        item.add(5)
        print(item, isinstance(item,set))

    elif isinstance(item, str):
        print('Str')
        print(item.upper())

    elif isinstance(item,(int, float)):
        print('Num')
        print(item,item * 2)

    else:
        print('Outro')
        print(item)
