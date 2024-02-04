"""
os.walk para navegar de caminhos de forma recursiva

os.walk é uma função que permite percorrer uma estrutura
de diretórios de maneira recursiva. Ela gera uma sequencia
de tuplas, onde cada tupla possui três elementos:
o diretorio atual (root), uma lista de subdiretórios (dirs)
e uma lista dos arquivos do diretório atual (files)
"""
import os
from itertools import count

caminho = os.path.join('/home','pedro-souza','Imagens')
counter = count()

for root, dirs, files in os.walk(caminho):
    print(root)
    print(dirs)
    print(files)