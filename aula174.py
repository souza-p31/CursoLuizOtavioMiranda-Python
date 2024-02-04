"""
os + shutil - Apagando, copiando, movendo e renomeando pastas, com Python

Vamos copiar arquivos de uma pasta para outra.

Copiar - shutil. copy

Copiar árvore recursivamente -> shutil.copytree

Apagando árvore recursivamente -> shutil.rmtree

Apagando arquivos -> shutil.move ou os.rename
"""
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Área de Trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
# shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_teste')

"""
Esse código bem menor faz a mesma coisa que o anterior.
"""