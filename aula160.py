"""
namedtuples - tuplas imutáveis com nomes para valores

Usamos namedtuples para criar classes de objetos que são
apenas um agrupamento de atributos, como classes normais
sem métodos, ou registros de bases de bases, etc.

As namedtuples são imutáveis assim como as tuplas.

# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
"""

from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'], 
                   defaults=['VALOR', 'NAIPE'])

as_de_espadas = Carta('A', 'Espada')

print(as_de_espadas._asdict())
print(as_de_espadas)
print(as_de_espadas[0])
print(as_de_espadas.valor)
print(as_de_espadas[1])
print(as_de_espadas.naipe)
print(as_de_espadas._fields)
print(as_de_espadas._field_defaults)

for valor in as_de_espadas:
    print(valor)