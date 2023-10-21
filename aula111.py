# map, partial, GeneratorType e esgotamento de Iterators

"""Como vimos antes, usando mapeando da list comprehension podemos fazer um deepcopy e modificar valores em um dicionário, porém com uma função do Python chamada map podemos fazer aquela mesma coisa porém de uma forma mais simples"""
from functools import partial
from types import GeneratorType

# def print_iter(iterator):
#     print(*list(iterator), sep='\n')
#     print()



# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]

# # Dessa forma conseguimos chegar no resultado das listas comprehension antes vistas. A função map recebe como parametro uma função e um iterável. Nesse caso eu apenas fiz uma lambda function, mas poderia usar qualquer outra função. O map retorna um iterator e pode ser esgotado, para contornar isso podemos colocar o map dentro de uma lista, para guardar os valores e usar sempre que quisermos. A função round eu coloquei apenas para arredondar os valors.

# def aumentar_porcentagem(valor, porcentagem):
#     return round(valor * porcentagem, 2) 

# # A função partial do modulo functools faz basicamente o que um clojure faz, ela recebe e guarda uma função e depois executa a função interna recebendo um valor. Nesse caso recebeu a função de aumentar porcentagem e só depois recebeu o valor da porcentagem.
# aumentar_dez_porcento = partial(
#     aumentar_porcentagem, porcentagem=1.1
# )


# # novos_produtos = [
# #     {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
# # ]

# def muda_preco_de_produto(produto):
#     return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

# novos_produtos = list(map(
#     muda_preco_de_produto,
#     produtos)
# )

# # Todo generator é um iterator, mas nem todo iterator é um generator. Para chegar se é ou não um generator podemos usar a função Generatortype do modulo types

# print(novos_produtos)
# print_iter(novos_produtos)
# print_iter(produtos)

# print(list)
# print(isinstance(novos_produtos, GeneratorType))


# Função partial, semelhante a um clojure
def soma(x, y):
    return x + y

a = partial(soma, 2)
print(a(8))

#Função map, semelhante ao mapeamento das list comprehension
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# podemos usar a função map combinada com a função partial, como fizemos com o list comprehension e clojure. Nesse caso aqui usei partial para "criar um clojure" que guarda o valor que vai aumentar, e dentro do map chamei a função com esse valor guardado e informei onde deveria ser aplicado, no caso na lista com os produtos.
def precos(lista, porcentagem):
    return round(lista['preco'] * porcentagem, 2)

porcentagem = partial(precos, porcentagem=1.1)

b = list(map(porcentagem, produtos))
print(b)