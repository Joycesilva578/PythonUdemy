caminho_arquivo = r'C:\\Users\\Joyce\\Documents\\PythonUdemy\\'
caminho_arquivo += 'aula65.txt'

#arquivo = open(caminho_arquivo, 'w')

#arquivo.close()

with open(caminho_arquivo,'w') as arquivo:
    arquivo.write('teste')