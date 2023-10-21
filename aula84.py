"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas
a partir de iteráveis
"""

# Jeito tradicional de fazer lista
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# Utilizando List Comprehension conseguimos fazer 
# A mesma coisa porém poupando linhas e de código e 
# tempo consequentemente

# Além de executar um for podemos colocar uma lógica à esquerda dele
# e paralelo a isso fazer um append na lista
lista = [numero for numero in range(10)]
# print(lista)

lista = [numero * 2 for numero in range(10)]
# print(lista)

lista = [numero * 3
         for numero in range(10)
         ]
# print(lista)

"""
Mapeamento de dados em list comprehension

Se pararmos para pensar, quando utilizamos a list
comprehension anteriormente, pegamos a lista original
que seria de 0 a 9 e multiplicamos por 2.
Então pela lógica vamos ter o mesmo número de elementos
na entrada e na saída, e isso está correto. É o chamado
mapeamento. Podemos utilizar isso para fazer algumas coisas, como:
"""

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    produto for produto in produtos
]
print(novos_produtos) # Nesse caso aqui eu só "copiei" os itens de uma lista para a outra sem alterar, mas ...

novos_produtos = [
    {produto['nome'], produto['preco'] * 1.05}
    for produto in produtos
]
print(novos_produtos) # Como em um dicionario só é possível ter uma unica chave por item
# fizemos a troca de todos eles com um aumento de 5%, mas também da pra aprimorar a list comprehension
# se depois do valor que ela irá receber colocarmos um if por exemplo. Para isso podemos usar operação ternária

novos_produtos = [
    {produto['nome'], produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos # o que vem à esquerda é mapeamento, o que vem a direita é filtro
    if produto['preco'] >= 20 and (produto['preco'] * 1.05) > 10]
print(novos_produtos)
print()
print(*novos_produtos, sep='\n') # E nesse caso aqui o valor só foi alterado se fosse maior que 20
