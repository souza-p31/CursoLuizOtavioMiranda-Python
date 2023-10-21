"""
Criando arquivos com Python + Content Manager with
Usamos a função open para abrir
Um arquivo em Python (ele pode ou não existir)

Modos:
r (leitura), w (escrita), x (criação)
a (escreve ao final/append mode), b (binário)
t (modo de texto), + (leitura e escrita)

Context Manager - with (abre e fecha)
Métodos úteis
Write, Read (escrever e ler)
Writelines (escrever várias linhas)
seek (mover o cursor)
readline (ler linha)
readlines (ler linhas)

Vamos falar mais sobre o módulo OS, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o módulo Json, mas:
json.dump - gera um arquivo json
json.load
"""

# caminho = 'C:\\Users\\ph324\\Documents\\curso_python'
# print(caminho)

caminho_arquivo = 'C:\\Users\\ph324\\Documents\\curso_python\\aula116.txt'

# forma 1 de criação de arquivo (sempre que abrir precisa fechar):
# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0,0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print('#' * 10)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())


# Como no charset que usamos aqui no Brasil tem acentuações precisamos ficar atentos na hora de criar arquivos de texto para evitar bugs, pra isso que serve o encoding. Da pra mudar também no VSCODE.
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

"""
A diferença entre 
Aten��o
Linha 1
Linha 2
E
Atenção
Linha 1
Linha 2
está no charset/encoding
"""

import os

# os.remove(caminho_arquivo)
# os.unlink(caminho_arquivo)
os.rename(caminho_arquivo,'aula116.txt')


"""
O formato json é para manipulação de dados, o nome significa Java Script Object Note, basicamente a estrutura dele pode ser identada indefinidamente. Ele usa uma estrutura de listas e dicionários:

pessoa = [{"nome": 'Pedro', "sobrenome": 'Souza'},
          {"nome": 'Augusto', "sobrenome": 'Oliveira'}]

O Json é bom para padronizar os dados para poder importar para diversos lugares. Para manipular json precisamos da biblioteca Json. As principais funções dela biblioteca são o Dump, Dumps, Load e Loads. Basicamente o que elas fazem sequencialmente é:

dump - pega uma estrutura e transforma em arquivo
dump - pega uma string e transforma em arquivo
load - carrega um json para dentro do programa
loads - carrega uma string json para dentro do programa
          """

