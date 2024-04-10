"""
Lista de listas e seus indices

"""

salas = [
     ['Maria', 'Helena', ],
     ['Joyce',],
     ['Luiz', 'Joao', 'Eduarda',(0,10,20,30,40)],


]
""" 
print(salas)
print(salas[0][1])
print(salas[1])
print(salas[2][2])
print(salas[2][3][2])
"""
for sala in salas:
     print(f'A sala é{sala}')
     for aluno in sala:
          print(aluno)
