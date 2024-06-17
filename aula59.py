
#exercicio como usar funcao zip e zip_longest

from itertools import zip_longest

l1 = ['Salvador','Ubatuba', 'Belo Horizonte']
l2 = ['Ba', 'SP', 'MG', 'RJ']

print(list(zip(l1,l2)))
print(list(zip_longest(l1,l2,fillvalue='SEM CIDADE')))