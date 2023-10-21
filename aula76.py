"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas com o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}
"""

# pessoa = dict(nome='Pedro', sobrenome='Souza')
# print(pessoa, type(pessoa))

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }

# # print(pessoa, type(pessoa))

# print(pessoa['nome'])
# print(pessoa['sobrenome'])

# print()

# for chave in pessoa:
#     print(chave, pessoa[chave])

# Manipulando chaves e valores em dicionários

# pessoa = {}

# chave = 'nome'

# pessoa[chave] = 'Luiz Otávio'
# pessoa['sobrenome'] = 'Miranda'

# print(pessoa[chave])

# print(pessoa['nome1']) # Se a chave não existe o Python vai retornar um keyerror
# print(pessoa['nome'], pessoa['sobrenome'])

# del pessoa['sobrenome']
# print(pessoa)
# print(pessoa['nome'])

# if pessoa['sobrenome']: # If quebra com erro. Da pra utilizar o metodo get pra contornar isso.
#     print('Existe')

# if pessoa.get('sobrenome', 'Não existe'): # Por padrão o get retorna None caso a chave não exista

# if pessoa.get('sobrenome') is None: # Por padrão o get retorna None caso a chave não exista
#     print('Não existe')
# else:
#     print('Existe')

"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 900
# }

# pessoa.setdefault('idade',0)
# print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# Shallow copy ou cópia rasa

# d1 = {
#     'c1': 1,
#     'c2': 2,
# }

# d2 = d1
# d2['c1'] = 1000
# print(d1)

# Fazendo dessa forma os dicionários são vinculados e quando um é alterado o outro também é

# d1 = {
#     'c1': 1,
#     'c2': 2,
# }

# d2 = d1.copy()
# d2['c1'] = 1000
# print(d1)
# print(d2)

# Usando o método copy acontece uma cópia rasa, e por conta disso eles não são vinculados e podem ser modificados separadamente

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2]
# }

# d2 = d1.copy()
# d2['c1'] = 1000
# d2['l1'][1] = 9999

# print(d1)
# print(d2)

# O copy faz uma cópia rasa das listas, e por isso ela continua conectada com o dicionário antigo. Para contornar isso existe um módulo no Python chamado copy

# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2]
# }

# d2 = copy.deepcopy(d1)
# d2['c1'] = 1000
# d2['l1'][1] = 9999

# print(d1)
# print(d2)

# Dessa forma acontece a copia profunda e não a copia rasa, e dessa forma criando uma copia verdadeira ate das listas sem qualquer vinculo.

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda'
}

# print(p1['nome'])
# print(p1.get('nome','Não existe')) # Tenta pegar uma chave e valor, mas caso ela não existe no lugar de dar um erro ele retorna None ou algum argumento.

# nome = p1.pop('nome') # Apaga a chave inserida e retorna ela
# print(nome)
# print(p1)

# ultima_chave = p1.popitem() # semelhante ao pop, pórem apaga o ultimo item inteiro
# print(ultima_chave)
# print(p1)

# Existem 3 formas de usar o update
p1.update({
    'nome': 'novo valor',
    'idade': 30
})

p1.update(nome='novo valor',idade=30)

tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)

# Todos fazem o mesmo, porém de formas diferentes