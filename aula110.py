# groupby - agrupando valores (itertools)

"""
Assim como em um banco de dados, podemos trazer um agrupador para dentro do Python usando a função groupby do modulo itertools. Ela vai receber um iterador e ordernar conforme a chave informada
"""
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# alunos_ordenados = groupby(alunos)
# print(alunos_ordenados) # Se fizermos assim, vai imprimir apenas o ID do iterador.
# print(list(alunos_ordenados)) # Aqui jogamos para uma lista para conseguir visualizar, mas a informação está ruim e confusa.

# Para visualizar da forma correta precisamos fazer assim

# alunos_ordenados = groupby(alunos, key=lambda a: a['nota'])
# # print(list(alunos_ordenados)) # Aqui já começamos a agrupar algo, mas ainda está ruim. Como dentro de cada tupla dentro da lista tem dois itens, isso nos leva a crer que se trata de um dicionario, nesse caso podemos acessar com um for chamando valor e chave.

# for chaves, alunos in alunos_ordenados:
#     print(chaves) # Porem dessa forma só veremos o iterador, podemos criar um for dentro do for para acessar o segundo iterador.
#     for aluno in alunos:
#         print(aluno) # Agora sim, já estamos conseguindo chegar em algum lugar, porém não agrupou da forma que a gente queria. Isso aconteceu porque antes de agrupar precisamos colocar na ordem, se não acontece isso.

alunos_ordenados = sorted(alunos, key=lambda a: a['nota'])
alunos_agrupados = groupby(alunos_ordenados, key=lambda a: a['nota'])

print(alunos_agrupados) # mesmo problema de antes, mas agora a gente já sabe resolver.

for chave, grupo in alunos_agrupados:
    print(chave)
    for pessoa in grupo:
        print(pessoa)

# pronto, agora sim. Depois de colocar na ordem e agrupar da forma correta temos o resultado que queriamos.