"""
os + shutil - Copiando arquivos com Python
Vamos copiar arquivos de uma pasta para outra.
Copiar -> shutil.copy
"""
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Área de Trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

os.makedirs(NOVA_PASTA, exist_ok=True)
os.makedirs(PASTA_ORIGINAL, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):

    for diretorio in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), diretorio)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)


    for f in files:
        caminho_arquivo = os.path.join(root, f)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA))
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)