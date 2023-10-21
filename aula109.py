"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa - iterável + tamanho do grupo
Permutação - Ordem importa
Produto - Ordem importa e repete valores únicos
"""

# São todos funções do modulo itertools e são funções muito úteis, vamos ver como funcionam.

from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino'],
    ['algodão', 'poliéster'],
]

print_iter(combinations(pessoas, 2)) # Combinações sem considerar a ordem, combinações unicas.

print_iter(permutations(pessoas, 2)) # Combinações considerando ordem, todas combinações possíveis.

print_iter(product(*camisetas)) # Todas as combinações possíveis entre itens de listas diferentes, considerando ordem e repetições.