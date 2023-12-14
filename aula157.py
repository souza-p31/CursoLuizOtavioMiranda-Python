"""
Enum -> Enumerações

Enumerações na programação, são usadas em ocasiões onde temos
um determinado número de coisas para escolher.

Enums tem membros e seus valores são constantes.

Enums em python:
    - são um conjunto de nomes simbólicos (membros) ligados a
    valores únicos.
    - podem ser iterados para retornar seus membros canônicos
    na ordem de definição.

enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
diretamente (mesmo assim, Enums não são classes normais em Python).

Você poderá usar seu Enum com type annotations, com isinstance e outras 
coisas relacionadas com tipo.

Para obter os dados:
membro = Classe(valor), Classe['chave']
chave = Classe.chave.name
valor = Classe.chave.value
"""
import enum

def mover(direcao):
    if direcao not in ['esquerda', 'direita']:
        raise ValueError('Lado inválido')
    print(f'Movendo para {direcao}')

mover('esquerda')
mover('direita')
# mover('acima')
# mover('abaixo')


# FORMA 1
direcoes = enum.Enum('Direções', ['ESQUERDA', 'DIREITA'])
print(direcoes(1), direcoes.ESQUERDA, direcoes['ESQUERDA'])
print(direcoes(1).name, direcoes.ESQUERDA.value, direcoes['ESQUERDA'])

def mover(direcao):
    if not isinstance(direcao, direcoes):
        raise ValueError('Direção não encontrada')
    print(f'Movendo para {direcao.name}')

mover(direcoes.ESQUERDA)
mover(direcoes(2))

# FORMA 2
class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    
    print(f'Movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.ESQUERDA)
mover(Direcoes(2))
mover(Direcoes['ACIMA'])
mover(Direcoes.ABAIXO)