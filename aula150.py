"""
Context Manager com função - Criando e Usando
gerenciadores de contexto
"""
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu o erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()
    
with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 4\n')
    arquivo.write('Linha 5\n')
    arquivo.write('Linha 6\n')
    print('With', arquivo)